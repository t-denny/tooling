.PHONY: all clean

all: clean prepare build

BIN_DIRECTORY := /home/buildbot/tools/disk-cleaner

.PHONY: clean
clean: ## clean all
        rm -fr ${BIN_DIRECTORY}

.PHONY: prepare
prepare:
        mkdir -p ${BIN_DIRECTORY}

.PHONY: build
build: ## build package
        cp clean_hj.sh $(BIN_DIRECTORY)
        cp clean_tmp.sh $(BIN_DIRECTORY)
        go build -o $(BIN_DIRECTORY)/disk-cleaner .