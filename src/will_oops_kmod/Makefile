obj-m := will_oops.o
KERNELDIR := /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

all:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules

clean:
	rm -rf modules.order Module.symvers *.ko *.o .depend .*.cmd *.mod.c .tmp_versions
