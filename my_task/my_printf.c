#include <stdio.h>
#include <unistd.h>
#include <stdarg.h>
#include <stdlib.h>

int my_putchar(char c) {
    return (write(1, &c, 1));
}

int my_put_str(char *str)
{
    int len = 0;

    if (str == NULL) {
        len += my_put_str("(null)");
        return len;
    }

    while (*str != '\0')
    {
        my_putchar(*str);
        len++;
        str++;
    }
    return (len);
}

int my_put_int(int n) {
    int len = 0;
    if (n < 0) {
        len += my_putchar('-');
        n = -n;
    }
    int divisor = 1;
    while (n / divisor >= 10)
        divisor *= 10;
    while (divisor != 0) {
        int digit = (n / divisor) % 10;
        len += my_putchar(digit + '0');
        divisor /= 10;
    }
    return len;
}

int my_put_octal(unsigned int n) {
    int len = 0;
    char octal[100];
    int i = 0;
    
    while (n != 0) {
        octal[i] = n % 8 + '0';
        n /= 8;
        i++;
    }
    
    for (int j = i - 1; j >= 0; j--) {
        my_putchar(octal[j]);
        len++;
    }
    
    return len;
}

int my_put_unsigned_int(unsigned int n) {
    int len = 0;
    
    if ((n / 10) != 0)
        len += my_put_unsigned_int(n / 10);
    len += my_putchar(n % 10 + '0');
    return (len);   
}

int my_put_x(unsigned long n)
{
    char hex_digits[] = "0123456789abcdef";
    char hex_arr[16] = {0};
    int i = 0;

    do {
        hex_arr[i++] = hex_digits[n % 16];
        n /= 16;
    } while (n > 0);

    for (int j = i - 1; j >= 0; j--) {
        if (hex_arr[j] >= 'a' && hex_arr[j] <= 'f') {
            hex_arr[j] -= 32;
        }
        my_putchar(hex_arr[j]);
    }
    return i;
}

int my_put_p(void *pointer) {
    char hex_digits[] = "0123456789abcdefABCDEF";// use upper case characters
    char hex_arr[16] = {0}; /* maximum length of hex string for unsigned int */
    int i = 0;
    unsigned long ppoint = (unsigned long)pointer;
    int len = 0;

    if (ppoint == 0) {
        len += my_put_str("(null)");
        return len;
    }

    do {
        hex_arr[i++] = hex_digits[ppoint % 16];
        ppoint /= 16;
    } while (ppoint > 0);

    len += my_put_str("0x");
    for (int j = i - 1; j >= 0; j--) {
        my_putchar(hex_arr[j]);
        len++;
    }

    return len;
}

int my_printf(char * restrict format, ...) {

    va_list args;
    int len = 0;

    va_start(args, format);

    for (int i = 0; format[i] != '\0'; i++) {
        if (format[i] == '%') {
            i++;
            switch (format[i]) {
                case 'd':
                    len += my_put_int(va_arg(args, int));
                    break;
                    
                case 'o':
                    len += my_put_octal(va_arg(args, unsigned int));
                    break;

                case 'u':
                    len += my_put_unsigned_int(va_arg(args, unsigned int));
                    break;

                case 'x':
                    len += my_put_x(va_arg(args, int));
                    break;
                    
                case 'c':
                    len += my_putchar(va_arg(args, int));
                    break;
                    
                case 's':
                    len += my_put_str(va_arg(args, char *));
                    break;
                
                case 'p':
                    len += my_put_p(va_arg(args, void *));
                    break;

                default:
                    my_putchar('%');
                    my_putchar(*format);
                    break;
            }
        }
        else
        {
            len += my_putchar(format[i]);
        }
    }
    va_end(args);

    return (len);
}

int main () {
    char * big = "big";
    my_printf("%d\n", my_printf("Hello %s %p\n", big, big));
    printf("%d\n", printf("Hello %s %p\n", big, big));
    return(0);
}
