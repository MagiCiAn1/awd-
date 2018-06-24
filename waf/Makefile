CC = gcc
NAME = mirage

$(NAME): main.o waf.o log.o
	$(CC) -o $(NAME) -pthread main.o waf.o log.o

main.o: main.c
	$(CC) -o main.o -c main.c

waf.o: waf.c waf.h
	$(CC) -o waf.o -c -lpthread waf.c

log.o: log.c log.h
	$(CC) -o log.o -c log.c

clean:
	rm *.o

