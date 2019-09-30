import os
import zipfile


def extract(zip_file, output_dir):
	f_zip = zipfile.ZipFile(zip_file, 'r')
	f_zip.extractall(output_dir)

extract(r"X:\9130_android\v1.5.103.2015_0927-183730.zip","d:/temp")