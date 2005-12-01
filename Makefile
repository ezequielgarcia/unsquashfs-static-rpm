# Makefile for source rpm: squashfs-tools
# $Id$
NAME := squashfs-tools
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
