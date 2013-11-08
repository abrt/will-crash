#include <iostream>

namespace Will
{
    class Fail
    {
    private:
        int value;
        void a() __attribute__ ((noinline))
        {
            char *s = NULL;

            std::cout << "Will segfault.\n";
            std::cout << s[666];
        }

    public:
        Fail(int x)
        {
            value = x;
        }

        int b() __attribute__ ((noinline))
        {
            a();
            return value;
        }
    };
}

int main(int argc, char *argv[])
{
    Will::Fail f = Will::Fail(1);
    f.b();

    return 0;
}
