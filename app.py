import os

import pydicom


def find_files(directory):
    """
    This function will recursively search for files
    :param directory:
    :return:
    """
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def extract_sequence(sequence):
    seq_data = []
    for dataset in sequence:
        item_data = {}
        for elem in dataset:
            if elem.VR == "SQ":
                item_data[elem.name] = extract_sequence(elem.value)
            else:
                item_data[elem.name] = str(elem.value)
        seq_data.append(item_data)
    return seq_data


def extract_all_dicom_data(file_path):
    dicom = pydicom.dcmread(file_path)
    data = {}

    for elem in dicom.iterall():
        if elem.VR != "SQ":  # Skip sequence items
            try:
                data[elem.name] = elem.value
            except:
                data[elem.name] = "Unable to extract"
        elif elem.VR == "SQ":
            data[elem.name] = extract_sequence(elem.value)

    data["PixelData"] = dicom.PixelData

    return data


directory_path = '/Users/andynguyen/Downloads/DICOMS'
files = find_files(directory_path)
for file in files:
    data = extract_all_dicom_data(file)
    print(data)
    # print(file)
