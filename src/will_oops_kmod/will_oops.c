#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>

MODULE_AUTHOR("ABRT Team <crash-catcher@lists.fedorahosted.org>");
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Causes kernel oops");

static int __init will_oops_init(void) {
        printk("will_oops loaded");
        WARN(true, "This kernel oops is brought to you by will_oops.");
        return 0;
}
static void __exit will_oops_exit(void) {
        printk("will_oops unloaded");
}

module_init(will_oops_init);
module_exit(will_oops_exit);
