EVERNOTE_DIR = ./evernote
EVERNOTE_SRC = $(wildcard $(EVERNOTE_DIR)/*.cpp)
EVERNOTE_INC = -I$(EVERNOTE_DIR)

STD        = c++11
SRCS_DIRS  = $(EVERNOTE_SRC)
INCS_DIRS  = $(EVERNOTE_INC) -I/usr/local/include
LIBS_DIRS  = -L/usr/local/lib
CPP_DEFS   = -D=HAVE_CONFIG_H
CPP_OPTS   = -Wall -O2
LIBS       = -lthrift

build: main.cpp
	g++ -std=$(STD) $(CPP_OPTS) $(CPP_DEFS) -o main $(INCS_DIRS) main.cpp $(SRCS_DIRS) $(LIBS_DIRS) $(LIBS)

clean:
	$(RM) -r main
