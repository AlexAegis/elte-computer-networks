""" Task 2
Create a TCP application what is capable of playing the guess game
all by itself
"""
import logging
import time
import exam_santa_server
import exam_santa_cache
import exam_santa_client


def run():
	"""
	Bootstrap the application
	"""
	logging.basicConfig(level="INFO")
	logging.info("\t\tBootstrapping application")

	server = exam_santa_server.Server({
	    "id": "server",
	    "host": "localhost",
	    "port": 11232,
	    "timeout": 5
	})

	santa = exam_santa_cache.Cache({
	    "id": "cache",
	    "host": "localhost",
	    "port": 11233,
	    "timeout": 5,
	    "server": server
	}, ["a", "b", "c", "d", "e", "f", "g", "h"])

	elf_a = exam_santa_client.Client({"id": "a", "server": santa})
	elf_b = exam_santa_client.Client({"id": "b", "server": santa})
	elf_c = exam_santa_client.Client({"id": "c", "server": santa})

	#server.start()
	santa.start()
	elf_a.start()
	elf_b.start()
	elf_c.start()


if __name__ == '__main__':
	run()
