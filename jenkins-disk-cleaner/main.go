package main

import (
	"fmt"
	"syscall"
	"math"
	"github.com/jasonlvhit/gocron"
	"os"
	"os/exec"
)

const (
	B  = 1
	KB = 1024 * B
	MB = 1024 * KB
	GB = 1024 * MB
	CLEAN_WHEN = 80 //in percents
)

var (
	partition = map[string]string{
		"/home/jenkins": "clean_hj.sh",
		"/tmp": "clean_tmp.sh",
	}
)

type DiskStatus struct {
	All  uint64 `json:"all"`
	Used uint64 `json:"used"`
	Free uint64 `json:"free"`
}

// disk usage of path/disk
func DiskUsage(path string) (disk DiskStatus) {
	fs := syscall.Statfs_t{}
	err := syscall.Statfs(path, &fs)
	if err != nil {
		return
	}
	disk.All = fs.Blocks * uint64(fs.Bsize)
	disk.Free = fs.Bfree * uint64(fs.Bsize)
	disk.Used = disk.All - disk.Free
	return
}

func CleanProcess(Comeng string) {
	cmd := &exec.Cmd {
		Path: Comeng,
		Args: []string{Comeng},
		Stdout: os.Stdout,
		Stderr: os.Stdout,
	}
	cmd.Start()
	cmd.Wait()
}

func CleanUp() {
	for key, element := range partition {
		disk := DiskUsage(key)
		fmt.Printf("=====Disk mounted on \"%s\"=====\n", key)
		percentage := math.Trunc(float64(disk.Used)/float64(disk.All) * 100)
		fmt.Printf("Current percentage: %g%%\n", percentage)
		if ( percentage > CLEAN_WHEN ) {
			fmt.Printf("\nExecuting %s...\n", element)
			CleanProcess(element)
		}
	}
}

func main() {
	fmt.Println("Running smart cleaner!")
	s := gocron.NewScheduler()
	s.Every(5).Minute().Do(CleanUp)
	<- s.Start()
}
