import re
import numpy

__bs_energy_bond_sep_regex = re.compile(' |-')


def process_energy(data: dict):
    new_data = dict()
    for el in data["data"]:
        key = tuple(__bs_energy_bond_sep_regex.split(el['bind']))
        del el['bind']
        new_data[key] = el
    return new_data


def Rj_mean(data:dict):
    Rj_list = list()
    for el in data['data']:
        Rj_list.append(el['R*j'])
    return numpy.mean(Rj_list)

def ek_mean(data:dict):
    ek_list = list()
    for el in data['data']:
        ek_list.append(el['e_k'])
    return numpy.mean(ek_list)


def K_r_mean(data: dict):
    K_r_list = list()
    for el in data['data']:
        K_r_list.append(el['K_r'])
    return numpy.mean(K_r_list)


def req_mean(data: dict):
    req_list = list()
    for el in data['data']:
        req_list.append(el['req'])
    return numpy.mean(req_list)


def K_q_mean(data: dict):
    K_r_list = list()
    for el in data['data']:
        K_r_list.append(el['K_q'])
    return numpy.mean(K_r_list)


def qeq_mean(data: dict):
    req_list = list()
    for el in data['data']:
        req_list.append(el['qeq'])
    return numpy.mean(req_list)


__bs_energy = {
    "data": [
        {"bind": "OW-HW", "K_r": 553.0, "req": 0.9572},
        {"bind": "HW-HW", "K_r": 553.0, "req": 1.5136},
        {"bind": "C-CA", "K_r": 469.0, "req": 1.409},
        {"bind": "C-CB", "K_r": 447.0, "req": 1.419},
        {"bind": "C-CM", "K_r": 410.0, "req": 1.444},
        {"bind": "C-CT", "K_r": 317.0, "req": 1.522},
        {"bind": "C-N*", "K_r": 424.0, "req": 1.383},
        {"bind": "C-NA", "K_r": 418.0, "req": 1.388},
        {"bind": "C-NC", "K_r": 457.0, "req": 1.358},
        {"bind": "C-O", "K_r": 570.0, "req": 1.229},
        {"bind": "C-O2", "K_r": 656.0, "req": 1.250},
        {"bind": "C-OH", "K_r": 450.0, "req": 1.364},
        {"bind": "CA-CA", "K_r": 469.0, "req": 1.400},
        {"bind": "CA-CB", "K_r": 469.0, "req": 1.404},
        {"bind": "CA-CM", "K_r": 427.0, "req": 1.433},
        {"bind": "CA-CT", "K_r": 317.0, "req": 1.510},
        {"bind": "CA-HA", "K_r": 367.0, "req": 1.080},
        {"bind": "CA-H4", "K_r": 367.0, "req": 1.080},
        {"bind": "CA-N2", "K_r": 481.0, "req": 1.340},
        {"bind": "CA-NA", "K_r": 427.0, "req": 1.381},
        {"bind": "CA-NC", "K_r": 483.0, "req": 1.339},
        {"bind": "CB-CB", "K_r": 520.0, "req": 1.370},
        {"bind": "CB-N*", "K_r": 436.0, "req": 1.374},
        {"bind": "CB-NB", "K_r": 414.0, "req": 1.391},
        {"bind": "CB-NC", "K_r": 461.0, "req": 1.354},
        {"bind": "CK-H5", "K_r": 367.0, "req": 1.080},
        {"bind": "CK-N*", "K_r": 440.0, "req": 1.371},
        {"bind": "CK-NB", "K_r": 529.0, "req": 1.304},
        {"bind": "CM-CM", "K_r": 549.0, "req": 1.350},
        {"bind": "CM-CT", "K_r": 317.0, "req": 1.510},
        {"bind": "CM-HA", "K_r": 367.0, "req": 1.080},
        {"bind": "CM-H4", "K_r": 367.0, "req": 1.080},
        {"bind": "CM-H5", "K_r": 367.0, "req": 1.080},
        {"bind": "CM-N*", "K_r": 448.0, "req": 1.365},
        {"bind": "CQ-H5", "K_r": 367.0, "req": 1.080},
        {"bind": "CQ-NC", "K_r": 502.0, "req": 1.324},
        {"bind": "CT-CT", "K_r": 310.0, "req": 1.526},
        {"bind": "CT-HC", "K_r": 340.0, "req": 1.090},
        {"bind": "CT-H1", "K_r": 340.0, "req": 1.090},
        {"bind": "CT-H2", "K_r": 340.0, "req": 1.090},
        {"bind": "CT-H3", "K_r": 340.0, "req": 1.090},
        {"bind": "CT-HP", "K_r": 340.0, "req": 1.090},
        {"bind": "CT-N*", "K_r": 337.0, "req": 1.475},
        {"bind": "CT-N2", "K_r": 337.0, "req": 1.463},
        {"bind": "CT-OH", "K_r": 320.0, "req": 1.410},
        {"bind": "CT-OS", "K_r": 320.0, "req": 1.410},
        {"bind": "H-N2", "K_r": 434.0, "req": 1.010},
        {"bind": "H-N*", "K_r": 434.0, "req": 1.010},
        {"bind": "H-NA", "K_r": 434.0, "req": 1.010},
        {"bind": "HO-OH", "K_r": 553.0, "req": 0.960},
        {"bind": "HO-OS", "K_r": 553.0, "req": 0.960},
        {"bind": "O2-P", "K_r": 525.0, "req": 1.480},
        {"bind": "OH-P", "K_r": 230.0, "req": 1.610},
        {"bind": "OS-P", "K_r": 230.0, "req": 1.610},
        {"bind": "C*-HC", "K_r": 367.0, "req": 1.080},
        {"bind": "C-N", "K_r": 490.0, "req": 1.335},
        {"bind": "C*-CB", "K_r": 388.0, "req": 1.459},
        {"bind": "C*-CT", "K_r": 317.0, "req": 1.495},
        {"bind": "C*-CW", "K_r": 546.0, "req": 1.352},
        {"bind": "CA-CN", "K_r": 469.0, "req": 1.400},
        {"bind": "CB-CN", "K_r": 447.0, "req": 1.419},
        {"bind": "CC-CT", "K_r": 317.0, "req": 1.504},
        {"bind": "CC-CV", "K_r": 512.0, "req": 1.375},
        {"bind": "CC-CW", "K_r": 518.0, "req": 1.371},
        {"bind": "CC-NA", "K_r": 422.0, "req": 1.385},
        {"bind": "CC-NB", "K_r": 410.0, "req": 1.394},
        {"bind": "CN-NA", "K_r": 428.0, "req": 1.380},
        {"bind": "CR-H5", "K_r": 367.0, "req": 1.080},
        {"bind": "CR-NA", "K_r": 477.0, "req": 1.343},
        {"bind": "CR-NB", "K_r": 488.0, "req": 1.335},
        {"bind": "CT-N", "K_r": 337.0, "req": 1.449},
        {"bind": "CT-N3", "K_r": 367.0, "req": 1.471},
        {"bind": "CT-S", "K_r": 227.0, "req": 1.810},
        {"bind": "CT-SH", "K_r": 237.0, "req": 1.810},
        {"bind": "CV-H4", "K_r": 367.0, "req": 1.080},
        {"bind": "CV-NB", "K_r": 410.0, "req": 1.394},
        {"bind": "CW-H4", "K_r": 367.0, "req": 1.080},
        {"bind": "CW-NA", "K_r": 427.0, "req": 1.381},
        {"bind": "H-N", "K_r": 434.0, "req": 1.010},
        {"bind": "H-N3", "K_r": 434.0, "req": 1.010},
        {"bind": "HS-SH", "K_r": 274.0, "req": 1.336},
        {"bind": "S-S", "K_r": 166.0, "req": 2.038},
        {"bind": "CT-F", "K_r": 367.0, "req": 1.380},
        # --------------------------------------------
        {"bind": "HW-OW", "K_r": 553.0, "req": 0.9572},
        {"bind": "HW-HW", "K_r": 553.0, "req": 1.5136},
        {"bind": "CA-C", "K_r": 469.0, "req": 1.409},
        {"bind": "CB-C", "K_r": 447.0, "req": 1.419},
        {"bind": "CM-C", "K_r": 410.0, "req": 1.444},
        {"bind": "CT-C", "K_r": 317.0, "req": 1.522},
        {"bind": "N*-C", "K_r": 424.0, "req": 1.383},
        {"bind": "NA-C", "K_r": 418.0, "req": 1.388},
        {"bind": "NC-C", "K_r": 457.0, "req": 1.358},
        {"bind": "O-C", "K_r": 570.0, "req": 1.229},
        {"bind": "O2-C", "K_r": 656.0, "req": 1.250},
        {"bind": "OH-C", "K_r": 450.0, "req": 1.364},
        {"bind": "CA-CA", "K_r": 469.0, "req": 1.400},
        {"bind": "CB-C", "K_r": 469.0, "req": 1.404},
        {"bind": "CM-CA", "K_r": 427.0, "req": 1.433},
        {"bind": "CT-CA", "K_r": 317.0, "req": 1.510},
        {"bind": "HA-CA", "K_r": 367.0, "req": 1.080},
        {"bind": "H4-CA", "K_r": 367.0, "req": 1.080},
        {"bind": "N2-CA", "K_r": 481.0, "req": 1.340},
        {"bind": "NA-CA", "K_r": 427.0, "req": 1.381},
        {"bind": "NC-CA", "K_r": 483.0, "req": 1.339},
        {"bind": "CB-CB", "K_r": 520.0, "req": 1.370},
        {"bind": "N*-CB", "K_r": 436.0, "req": 1.374},
        {"bind": "NB-CB", "K_r": 414.0, "req": 1.391},
        {"bind": "NC-CB", "K_r": 461.0, "req": 1.354},
        {"bind": "H5-CK", "K_r": 367.0, "req": 1.080},
        {"bind": "N*-CK", "K_r": 440.0, "req": 1.371},
        {"bind": "NB-CK", "K_r": 529.0, "req": 1.304},
        {"bind": "CM-CM", "K_r": 549.0, "req": 1.350},
        {"bind": "CT-CM", "K_r": 317.0, "req": 1.510},
        {"bind": "HA-CM", "K_r": 367.0, "req": 1.080},
        {"bind": "H4-CM", "K_r": 367.0, "req": 1.080},
        {"bind": "H5-CM", "K_r": 367.0, "req": 1.080},
        {"bind": "N*-CM", "K_r": 448.0, "req": 1.365},
        {"bind": "H5-CQ", "K_r": 367.0, "req": 1.080},
        {"bind": "NC-CQ", "K_r": 502.0, "req": 1.324},
        {"bind": "CT-CT", "K_r": 310.0, "req": 1.526},
        {"bind": "HC-CT", "K_r": 340.0, "req": 1.090},
        {"bind": "H1-CT", "K_r": 340.0, "req": 1.090},
        {"bind": "H2-CT", "K_r": 340.0, "req": 1.090},
        {"bind": "H3-CT", "K_r": 340.0, "req": 1.090},
        {"bind": "HP-CT", "K_r": 340.0, "req": 1.090},
        {"bind": "N*-CT", "K_r": 337.0, "req": 1.475},
        {"bind": "N2-CT", "K_r": 337.0, "req": 1.463},
        {"bind": "OH-CT", "K_r": 320.0, "req": 1.410},
        {"bind": "OS-CT", "K_r": 320.0, "req": 1.410},
        {"bind": "N2-H", "K_r": 434.0, "req": 1.010},
        {"bind": "N*-H", "K_r": 434.0, "req": 1.010},
        {"bind": "NA-H", "K_r": 434.0, "req": 1.010},
        {"bind": "OH-HO", "K_r": 553.0, "req": 0.960},
        {"bind": "OS-HO", "K_r": 553.0, "req": 0.960},
        {"bind": "P-O2", "K_r": 525.0, "req": 1.480},
        {"bind": "P-OH", "K_r": 230.0, "req": 1.610},
        {"bind": "P-OS", "K_r": 230.0, "req": 1.610},
        {"bind": "HC-C*", "K_r": 367.0, "req": 1.080},
        {"bind": "N-C", "K_r": 490.0, "req": 1.335},
        {"bind": "CB-C*", "K_r": 388.0, "req": 1.459},
        {"bind": "CT-C*", "K_r": 317.0, "req": 1.495},
        {"bind": "CW-C*", "K_r": 546.0, "req": 1.352},
        {"bind": "CN-CA", "K_r": 469.0, "req": 1.400},
        {"bind": "CN-CB", "K_r": 447.0, "req": 1.419},
        {"bind": "CT-CC", "K_r": 317.0, "req": 1.504},
        {"bind": "CB-CC", "K_r": 512.0, "req": 1.375},
        {"bind": "CW-CC", "K_r": 518.0, "req": 1.371},
        {"bind": "NA-CC", "K_r": 422.0, "req": 1.385},
        {"bind": "NB-CC", "K_r": 410.0, "req": 1.394},
        {"bind": "NA-CN", "K_r": 428.0, "req": 1.380},
        {"bind": "H5-CR", "K_r": 367.0, "req": 1.080},
        {"bind": "NA-CR", "K_r": 477.0, "req": 1.343},
        {"bind": "NB-CR", "K_r": 488.0, "req": 1.335},
        {"bind": "N-CT", "K_r": 337.0, "req": 1.449},
        {"bind": "N3-CT", "K_r": 367.0, "req": 1.471},
        {"bind": "S-CT", "K_r": 227.0, "req": 1.810},
        {"bind": "SH-CT", "K_r": 237.0, "req": 1.810},
        {"bind": "H4-CV", "K_r": 367.0, "req": 1.080},
        {"bind": "NB-CV", "K_r": 410.0, "req": 1.394},
        {"bind": "H4-CW", "K_r": 367.0, "req": 1.080},
        {"bind": "NA-CW", "K_r": 427.0, "req": 1.381},
        {"bind": "N-H", "K_r": 434.0, "req": 1.010},
        {"bind": "N3-H", "K_r": 434.0, "req": 1.010},
        {"bind": "SH-HS", "K_r": 274.0, "req": 1.336},
        {"bind": "S-S", "K_r": 166.0, "req": 2.038},
        {"bind": "F-CT", "K_r": 367.0, "req": 1.380}
    ]
}

__bending_energy = {
    "data": [
        {"bind": "HW-OW-HW", "K_q": 100.0, "qeq": 104.52},
        {"bind": "HW-HW-OW", "K_q": 0.0, "qeq": 127.74},
        {"bind": "CB-C-NA ", "K_q": 70.0, "qeq": 111.30},
        {"bind": "CB-C -O ", "K_q": 80.0, "qeq": 128.80},
        {"bind": "CM-C -NA", "K_q": 70.0, "qeq": 114.10},
        {"bind": "CM-C -O ", "K_q": 80.0, "qeq": 125.30},
        {"bind": "CT-C -O ", "K_q": 80.0, "qeq": 120.40},
        {"bind": "CT-C -O2", "K_q": 70.0, "qeq": 117.00},
        {"bind": "CT-C -OH", "K_q": 70.0, "qeq": 117.00},
        {"bind": "N*-C -NA", "K_q": 70.0, "qeq": 115.40},
        {"bind": "N*-C -NC", "K_q": 70.0, "qeq": 118.60},
        {"bind": "N*-C -O ", "K_q": 80.0, "qeq": 120.90},
        {"bind": "NA-C -O ", "K_q": 80.0, "qeq": 120.60},
        {"bind": "NC-C -O ", "K_q": 80.0, "qeq": 122.50},
        {"bind": "CT-C -N ", "K_q": 70.0, "qeq": 116.60},
        {"bind": "N -C -O ", "K_q": 80.0, "qeq": 122.90},
        {"bind": "O -C -O ", "K_q": 80.0, "qeq": 126.00},
        {"bind": "O2-C -O2", "K_q": 80.0, "qeq": 126.00},
        {"bind": "O -C -OH", "K_q": 80.0, "qeq": 126.00},
        {"bind": "CA-C -CA", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CA-C -OH", "K_q": 70.0, "qeq": 120.00},
        {"bind": "C -CA-CA", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CA-CA-CA", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CA-CA-CB", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CA-CA-CT", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CA-CA-HA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CA-CA-H4", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CB-CA-HA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CB-CA-H4", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CB-CA-N2", "K_q": 70.0, "qeq": 123.50},
        {"bind": "CB-CA-NC", "K_q": 70.0, "qeq": 117.30},
        {"bind": "CM-CA-N2", "K_q": 70.0, "qeq": 120.10},
        {"bind": "CM-CA-NC", "K_q": 70.0, "qeq": 121.50},
        {"bind": "N2-CA-NA", "K_q": 70.0, "qeq": 116.00},
        {"bind": "N2-CA-NC", "K_q": 70.0, "qeq": 119.30},
        {"bind": "NA-CA-NC", "K_q": 70.0, "qeq": 123.30},
        {"bind": "C -CA-HA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "N2-CA-N2", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CN-CA-HA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CA-CA-CN", "K_q": 63.0, "qeq": 120.00},
        {"bind": "C -CB-CB", "K_q": 63.0, "qeq": 119.20},
        {"bind": "C -CB-NB", "K_q": 70.0, "qeq": 130.00},
        {"bind": "CA-CB-CB", "K_q": 63.0, "qeq": 117.30},
        {"bind": "CA-CB-NB", "K_q": 70.0, "qeq": 132.40},
        {"bind": "CB-CB-N*", "K_q": 70.0, "qeq": 106.20},
        {"bind": "CB-CB-NB", "K_q": 70.0, "qeq": 110.40},
        {"bind": "CB-CB-NC", "K_q": 70.0, "qeq": 127.70},
        {"bind": "N*-CB-NC", "K_q": 70.0, "qeq": 126.20},
        {"bind": "C*-CB-CA", "K_q": 63.0, "qeq": 134.90},
        {"bind": "C*-CB-CN", "K_q": 63.0, "qeq": 108.80},
        {"bind": "CA-CB-CN", "K_q": 63.0, "qeq": 116.20},
        {"bind": "H5-CK-N*", "K_q": 35.0, "qeq": 123.05},
        {"bind": "H5-CK-NB", "K_q": 35.0, "qeq": 123.05},
        {"bind": "N*-CK-NB", "K_q": 70.0, "qeq": 113.90},
        {"bind": "C -CM-CM", "K_q": 63.0, "qeq": 120.70},
        {"bind": "C -CM-CT", "K_q": 70.0, "qeq": 119.70},
        {"bind": "C -CM-HA", "K_q": 35.0, "qeq": 119.70},
        {"bind": "C -CM-H4", "K_q": 35.0, "qeq": 119.70},
        {"bind": "CA-CM-CM", "K_q": 63.0, "qeq": 117.00},
        {"bind": "CA-CM-HA", "K_q": 35.0, "qeq": 123.30},
        {"bind": "CA-CM-H4", "K_q": 35.0, "qeq": 123.30},
        {"bind": "CM-CM-CT", "K_q": 70.0, "qeq": 119.70},
        {"bind": "CM-CM-HA", "K_q": 35.0, "qeq": 119.70},
        {"bind": "CM-CM-H4", "K_q": 35.0, "qeq": 119.70},
        {"bind": "CM-CM-N*", "K_q": 70.0, "qeq": 121.20},
        {"bind": "H4-CM-N*", "K_q": 35.0, "qeq": 119.10},
        {"bind": "H5-CQ-NC", "K_q": 35.0, "qeq": 115.45},
        {"bind": "NC-CQ-NC", "K_q": 70.0, "qeq": 129.10},
        {"bind": "CM-CT-HC", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-CT", "K_q": 40.0, "qeq": 109.50},
        {"bind": "CT-CT-HC", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-H1", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-H2", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-HP", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-N*", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-OH", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-OS", "K_q": 50.0, "qeq": 109.50},
        {"bind": "HC-CT-HC", "K_q": 35.0, "qeq": 109.50},
        {"bind": "H1-CT-H1", "K_q": 35.0, "qeq": 109.50},
        {"bind": "HP-CT-HP", "K_q": 35.0, "qeq": 109.50},
        {"bind": "H2-CT-N*", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-N*", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-OH", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-OS", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H2-CT-OS", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N*-CT-OS", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-N ", "K_q": 50.0, "qeq": 109.50},
        {"bind": "C -CT-H1", "K_q": 50.0, "qeq": 109.50},
        {"bind": "C -CT-HP", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-S ", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-SH", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-S ", "K_q": 50.0, "qeq": 114.70},
        {"bind": "CT-CT-SH", "K_q": 50.0, "qeq": 108.60},
        {"bind": "H2-CT-H2", "K_q": 35.0, "qeq": 109.50},
        {"bind": "H1-CT-N2", "K_q": 50.0, "qeq": 109.50},
        {"bind": "HP-CT-N3", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CA-CT-CT", "K_q": 63.0, "qeq": 114.00},
        {"bind": "C -CT-HC", "K_q": 50.0, "qeq": 109.50},
        {"bind": "C -CT-N ", "K_q": 63.0, "qeq": 110.10},
        {"bind": "CT-CT-N2", "K_q": 80.0, "qeq": 111.20},
        {"bind": "CT-CT-N ", "K_q": 80.0, "qeq": 109.70},
        {"bind": "C -CT-CT", "K_q": 63.0, "qeq": 111.10},
        {"bind": "CA-CT-HC", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-N3", "K_q": 80.0, "qeq": 111.20},
        {"bind": "CC-CT-CT", "K_q": 63.0, "qeq": 113.10},
        {"bind": "CC-CT-HC", "K_q": 50.0, "qeq": 109.50},
        {"bind": "C -CT-N3", "K_q": 80.0, "qeq": 111.20},
        {"bind": "C*-CT-CT", "K_q": 63.0, "qeq": 115.60},
        {"bind": "C*-CT-HC", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CC-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CT-CC-CV", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CT-CC-NB", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CV-CC-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CW-CC-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CW-CC-NB", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CT-CC-CW", "K_q": 70.0, "qeq": 120.00},
        {"bind": "H5-CR-NA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H5-CR-NB", "K_q": 35.0, "qeq": 120.00},
        {"bind": "NA-CR-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NA-CR-NB", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CC-CV-H4", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CC-CV-NB", "K_q": 70.0, "qeq": 120.00},
        {"bind": "H4-CV-NB", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CC-CW-H4", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CC-CW-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "H4-CW-NA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "C*-CW-H4", "K_q": 35.0, "qeq": 120.00},
        {"bind": "C*-CW-NA", "K_q": 70.0, "qeq": 108.70},
        {"bind": "CT-C*-CW", "K_q": 70.0, "qeq": 125.00},
        {"bind": "CB-C*-CT", "K_q": 70.0, "qeq": 128.60},
        {"bind": "CB-C*-CW", "K_q": 63.0, "qeq": 106.40},
        {"bind": "CA-CN-NA", "K_q": 70.0, "qeq": 132.80},
        {"bind": "CB-CN-NA", "K_q": 70.0, "qeq": 104.40},
        {"bind": "CA-CN-CB", "K_q": 63.0, "qeq": 122.70},
        {"bind": "C -N -CT", "K_q": 50.0, "qeq": 121.90},
        {"bind": "C -N -H ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "CT-N -H ", "K_q": 30.0, "qeq": 118.04},
        {"bind": "CT-N -CT", "K_q": 50.0, "qeq": 118.00},
        {"bind": "H -N -H ", "K_q": 35.0, "qeq": 120.00},
        {"bind": "C -N*-CM", "K_q": 70.0, "qeq": 121.60},
        {"bind": "C -N*-CT", "K_q": 70.0, "qeq": 117.60},
        {"bind": "C -N*-H ", "K_q": 30.0, "qeq": 119.20},
        {"bind": "CB-N*-CK", "K_q": 70.0, "qeq": 105.40},
        {"bind": "CB-N*-CT", "K_q": 70.0, "qeq": 125.80},
        {"bind": "CB-N*-H ", "K_q": 30.0, "qeq": 125.80},
        {"bind": "CK-N*-CT", "K_q": 70.0, "qeq": 128.80},
        {"bind": "CK-N*-H ", "K_q": 30.0, "qeq": 128.80},
        {"bind": "CM-N*-CT", "K_q": 70.0, "qeq": 121.20},
        {"bind": "CM-N*-H ", "K_q": 30.0, "qeq": 121.20},
        {"bind": "CA-N2-H ", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H -N2-H ", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CT-N2-H ", "K_q": 35.0, "qeq": 118.40},
        {"bind": "CA-N2-CT", "K_q": 50.0, "qeq": 123.20},
        {"bind": "CT-N3-H ", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-N3-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H -N3-H ", "K_q": 35.0, "qeq": 109.50},
        {"bind": "C -NA-C ", "K_q": 70.0, "qeq": 126.40},
        {"bind": "C -NA-CA", "K_q": 70.0, "qeq": 125.20},
        {"bind": "C -NA-H ", "K_q": 30.0, "qeq": 116.80},
        {"bind": "CA-NA-H ", "K_q": 30.0, "qeq": 118.00},
        {"bind": "CC-NA-CR", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CC-NA-H ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "CR-NA-CW", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CR-NA-H ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "CW-NA-H ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "CN-NA-CW", "K_q": 70.0, "qeq": 111.60},
        {"bind": "CN-NA-H ", "K_q": 30.0, "qeq": 123.10},
        {"bind": "CB-NB-CK", "K_q": 70.0, "qeq": 103.80},
        {"bind": "CC-NB-CR", "K_q": 70.0, "qeq": 117.00},
        {"bind": "CR-NB-CV", "K_q": 70.0, "qeq": 117.00},
        {"bind": "C -NC-CA", "K_q": 70.0, "qeq": 120.50},
        {"bind": "CA-NC-CB", "K_q": 70.0, "qeq": 112.20},
        {"bind": "CA-NC-CQ", "K_q": 70.0, "qeq": 118.60},
        {"bind": "CB-NC-CQ", "K_q": 70.0, "qeq": 111.00},
        {"bind": "C -OH-HO", "K_q": 35.0, "qeq": 113.00},
        {"bind": "CT-OH-HO", "K_q": 55.0, "qeq": 108.50},
        {"bind": "HO-OH-P ", "K_q": 45.0, "qeq": 108.50},
        {"bind": "CT-OS-CT", "K_q": 60.0, "qeq": 109.50},
        {"bind": "CT-OS-P ", "K_q": 100.0, "qeq": 120.50},
        {"bind": "P -OS-P ", "K_q": 100.0, "qeq": 120.50},
        {"bind": "O2-P -OH", "K_q": 45.0, "qeq": 108.23},
        {"bind": "O2-P -O2", "K_q": 140.0, "qeq": 119.90},
        {"bind": "O2-P -OS", "K_q": 100.0, "qeq": 108.23},
        {"bind": "OH-P -OS", "K_q": 45.0, "qeq": 102.60},
        {"bind": "OS-P -OS", "K_q": 45.0, "qeq": 102.60},
        {"bind": "CT-S -CT", "K_q": 62.0, "qeq": 98.90},
        {"bind": "CT-S -S ", "K_q": 68.0, "qeq": 103.70},
        {"bind": "CT-SH-HS", "K_q": 43.0, "qeq": 96.00},
        {"bind": "HS-SH-HS", "K_q": 35.0, "qeq": 92.07},
        {"bind": "F -CT-F ", "K_q": 77.0, "qeq": 109.10},
        {"bind": "F -CT-H1", "K_q": 35.0, "qeq": 109.50},
        # --------------------------------------------
        {"bind": "HW-OW-HW", "K_q": 100.0, "qeq": 104.52},
        {"bind": "OW-HW-HW", "K_q": 0.0, "qeq": 127.74},
        {"bind": "NA-C-CB ", "K_q": 70.0, "qeq": 111.30},
        {"bind": "O-C-CB ", "K_q": 80.0, "qeq": 128.80},
        {"bind": "NA-C-CM", "K_q": 70.0, "qeq": 114.10},
        {"bind": "O-C-CM ", "K_q": 80.0, "qeq": 125.30},
        {"bind": "O-C-CT ", "K_q": 80.0, "qeq": 120.40},
        {"bind": "O2-C-CT", "K_q": 70.0, "qeq": 117.00},
        {"bind": "OH-C-CT", "K_q": 70.0, "qeq": 117.00},
        {"bind": "NA-C-N*", "K_q": 70.0, "qeq": 115.40},
        {"bind": "NC-C-N*", "K_q": 70.0, "qeq": 118.60},
        {"bind": "O-C-N* ", "K_q": 80.0, "qeq": 120.90},
        {"bind": "O-C-NA ", "K_q": 80.0, "qeq": 120.60},
        {"bind": "O-C-NC ", "K_q": 80.0, "qeq": 122.50},
        {"bind": "N-C-CT ", "K_q": 70.0, "qeq": 116.60},
        {"bind": "O-C-N ", "K_q": 80.0, "qeq": 122.90},
        {"bind": "O -C -O ", "K_q": 80.0, "qeq": 126.00},
        {"bind": "O2-C -O2", "K_q": 80.0, "qeq": 126.00},
        {"bind": "OH-C-O", "K_q": 80.0, "qeq": 126.00},
        {"bind": "CA-C -CA", "K_q": 63.0, "qeq": 120.00},
        {"bind": "OH-C-CA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CA-CA-C", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CA-CA-CA", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CB-CA-CA", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CT-CA-CA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "HA-CA-CA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H4-CA-CA", "K_q": 35.0, "qeq": 120.00},
        {"bind": "HA-CA-CB", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H4-CA-CB", "K_q": 35.0, "qeq": 120.00},
        {"bind": "N2-CA-CB", "K_q": 70.0, "qeq": 123.50},
        {"bind": "NC-CA-CB", "K_q": 70.0, "qeq": 117.30},
        {"bind": "N2-CA-CM", "K_q": 70.0, "qeq": 120.10},
        {"bind": "NC-CA-CM", "K_q": 70.0, "qeq": 121.50},
        {"bind": "NA-CA-N2", "K_q": 70.0, "qeq": 116.00},
        {"bind": "NC-CA-N2", "K_q": 70.0, "qeq": 119.30},
        {"bind": "NC-CA-NA", "K_q": 70.0, "qeq": 123.30},
        {"bind": "HA-CA-C", "K_q": 35.0, "qeq": 120.00},
        {"bind": "N2-CA-N2", "K_q": 70.0, "qeq": 120.00},
        {"bind": "HA-CA-CN", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CN-CA-CA", "K_q": 63.0, "qeq": 120.00},
        {"bind": "CB-CB-C", "K_q": 63.0, "qeq": 119.20},
        {"bind": "NB-CB-C", "K_q": 70.0, "qeq": 130.00},
        {"bind": "CB-CB-CA", "K_q": 63.0, "qeq": 117.30},
        {"bind": "NB-CB-CA", "K_q": 70.0, "qeq": 132.40},
        {"bind": "N*-CB-CB", "K_q": 70.0, "qeq": 106.20},
        {"bind": "NB-CB-CB", "K_q": 70.0, "qeq": 110.40},
        {"bind": "NC-CB-CB", "K_q": 70.0, "qeq": 127.70},
        {"bind": "NC-CB-N*", "K_q": 70.0, "qeq": 126.20},
        {"bind": "CA-CB-C*", "K_q": 63.0, "qeq": 134.90},
        {"bind": "CN-CB-C*", "K_q": 63.0, "qeq": 108.80},
        {"bind": "CN-CB-CA", "K_q": 63.0, "qeq": 116.20},
        {"bind": "N*-CK-H5", "K_q": 35.0, "qeq": 123.05},
        {"bind": "NB-CK-H5", "K_q": 35.0, "qeq": 123.05},
        {"bind": "NB-CK-N*", "K_q": 70.0, "qeq": 113.90},
        {"bind": "CM-CM-C", "K_q": 63.0, "qeq": 120.70},
        {"bind": "CT-CM-C", "K_q": 70.0, "qeq": 119.70},
        {"bind": "HA-CM-C", "K_q": 35.0, "qeq": 119.70},
        {"bind": "H4-CM-C", "K_q": 35.0, "qeq": 119.70},
        {"bind": "CM-CM-CA", "K_q": 63.0, "qeq": 117.00},
        {"bind": "HA-CM-CA", "K_q": 35.0, "qeq": 123.30},
        {"bind": "H4-CM-CA", "K_q": 35.0, "qeq": 123.30},
        {"bind": "CT-CM-CM", "K_q": 70.0, "qeq": 119.70},
        {"bind": "HA-CM-CM", "K_q": 35.0, "qeq": 119.70},
        {"bind": "H4-CM-CM", "K_q": 35.0, "qeq": 119.70},
        {"bind": "N*-CM-CM", "K_q": 70.0, "qeq": 121.20},
        {"bind": "N*-CM-H4", "K_q": 35.0, "qeq": 119.10},
        {"bind": "NC-CQ-H5", "K_q": 35.0, "qeq": 115.45},
        {"bind": "NC-CQ-NC", "K_q": 70.0, "qeq": 129.10},
        {"bind": "HC-CT-CM", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-CT", "K_q": 40.0, "qeq": 109.50},
        {"bind": "HC-CT-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H2-CT-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "HP-CT-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N*-CT-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "OH-CT-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "OS-CT-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "HC-CT-HC", "K_q": 35.0, "qeq": 109.50},
        {"bind": "H1-CT-H1", "K_q": 35.0, "qeq": 109.50},
        {"bind": "HP-CT-HP", "K_q": 35.0, "qeq": 109.50},
        {"bind": "N*-CT-H2", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N*-CT-H1", "K_q": 50.0, "qeq": 109.50},
        {"bind": "OH-CT-H1", "K_q": 50.0, "qeq": 109.50},
        {"bind": "OS-CT-H1", "K_q": 50.0, "qeq": 109.50},
        {"bind": "OS-CT-H2", "K_q": 50.0, "qeq": 109.50},
        {"bind": "OS-CT-N*", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N-CT-H1 ", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H1-CT-C", "K_q": 50.0, "qeq": 109.50},
        {"bind": "HP-CT-C", "K_q": 50.0, "qeq": 109.50},
        {"bind": "S-CT-H1 ", "K_q": 50.0, "qeq": 109.50},
        {"bind": "SH-CT-H1", "K_q": 50.0, "qeq": 109.50},
        {"bind": "S-CT-CT ", "K_q": 50.0, "qeq": 114.70},
        {"bind": "SH-CT-CT", "K_q": 50.0, "qeq": 108.60},
        {"bind": "H2-CT-H2", "K_q": 35.0, "qeq": 109.50},
        {"bind": "N2-CT-H1", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N3-CT-HP", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-CT-CA", "K_q": 63.0, "qeq": 114.00},
        {"bind": "HC-CT-C", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N-CT-C ", "K_q": 63.0, "qeq": 110.10},
        {"bind": "N2-CT-CT", "K_q": 80.0, "qeq": 111.20},
        {"bind": "N-CT-CT ", "K_q": 80.0, "qeq": 109.70},
        {"bind": "CT-CT-C", "K_q": 63.0, "qeq": 111.10},
        {"bind": "HC-CT-CA", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N3-CT-CT", "K_q": 80.0, "qeq": 111.20},
        {"bind": "CT-CT-CC", "K_q": 63.0, "qeq": 113.10},
        {"bind": "HC-CT-CC", "K_q": 50.0, "qeq": 109.50},
        {"bind": "N3-CT-C", "K_q": 80.0, "qeq": 111.20},
        {"bind": "CT-CT-C*", "K_q": 63.0, "qeq": 115.60},
        {"bind": "HC-CT-C*", "K_q": 50.0, "qeq": 109.50},
        {"bind": "NA-CC-CT", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CV-CC-CT", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NB-CC-CT", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NA-CC-CV", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CW-CC-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NB-CC-CW", "K_q": 70.0, "qeq": 120.00},
        {"bind": "CW-CC-CT", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NA-CR-H5", "K_q": 35.0, "qeq": 120.00},
        {"bind": "NB-CR-H5", "K_q": 35.0, "qeq": 120.00},
        {"bind": "NA-CR-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NB-CR-NA", "K_q": 70.0, "qeq": 120.00},
        {"bind": "H4-CV-CC", "K_q": 35.0, "qeq": 120.00},
        {"bind": "NB-CV-CC", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NB-CV-H4", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H4-CW-CC", "K_q": 35.0, "qeq": 120.00},
        {"bind": "NA-CW-CC", "K_q": 70.0, "qeq": 120.00},
        {"bind": "NA-CW-H4", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H4-CW-C*", "K_q": 35.0, "qeq": 120.00},
        {"bind": "NA-CW-C*", "K_q": 70.0, "qeq": 108.70},
        {"bind": "CW-C*-CT", "K_q": 70.0, "qeq": 125.00},
        {"bind": "CT-C*-CB", "K_q": 70.0, "qeq": 128.60},
        {"bind": "CW-C*-CB", "K_q": 63.0, "qeq": 106.40},
        {"bind": "NA-CN-CA", "K_q": 70.0, "qeq": 132.80},
        {"bind": "NA-CN-CB", "K_q": 70.0, "qeq": 104.40},
        {"bind": "CB-CN-CA", "K_q": 63.0, "qeq": 122.70},
        {"bind": "CT-N-C", "K_q": 50.0, "qeq": 121.90},
        {"bind": "H-N-C ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "H-N-CT ", "K_q": 30.0, "qeq": 118.04},
        {"bind": "CT-N -CT", "K_q": 50.0, "qeq": 118.00},
        {"bind": "H -N -H ", "K_q": 35.0, "qeq": 120.00},
        {"bind": "CM-N*-C", "K_q": 70.0, "qeq": 121.60},
        {"bind": "CT-N*-C", "K_q": 70.0, "qeq": 117.60},
        {"bind": "H-N*-C ", "K_q": 30.0, "qeq": 119.20},
        {"bind": "CK-N*-CB", "K_q": 70.0, "qeq": 105.40},
        {"bind": "CT-N*-CB", "K_q": 70.0, "qeq": 125.80},
        {"bind": "H-N*-CB ", "K_q": 30.0, "qeq": 125.80},
        {"bind": "CT-N*-CK", "K_q": 70.0, "qeq": 128.80},
        {"bind": "H-N*-CK ", "K_q": 30.0, "qeq": 128.80},
        {"bind": "CT-N*-CM", "K_q": 70.0, "qeq": 121.20},
        {"bind": "H-N*-CM ", "K_q": 30.0, "qeq": 121.20},
        {"bind": "H-N2-CA ", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H -N2-H ", "K_q": 35.0, "qeq": 120.00},
        {"bind": "H-N2-CT ", "K_q": 35.0, "qeq": 118.40},
        {"bind": "CT-N2-CA", "K_q": 50.0, "qeq": 123.20},
        {"bind": "H-N3-CT ", "K_q": 50.0, "qeq": 109.50},
        {"bind": "CT-N3-CT", "K_q": 50.0, "qeq": 109.50},
        {"bind": "H -N3-H ", "K_q": 35.0, "qeq": 109.50},
        {"bind": "C -NA-C ", "K_q": 70.0, "qeq": 126.40},
        {"bind": "CA-NA-C", "K_q": 70.0, "qeq": 125.20},
        {"bind": "H-NA-C", "K_q": 30.0, "qeq": 116.80},
        {"bind": "H-NA-CA ", "K_q": 30.0, "qeq": 118.00},
        {"bind": "CR-NA-CC", "K_q": 70.0, "qeq": 120.00},
        {"bind": "H-NA-CC ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "CW-NA-CR", "K_q": 70.0, "qeq": 120.00},
        {"bind": "H-NA-CR ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "H-NA-CW ", "K_q": 30.0, "qeq": 120.00},
        {"bind": "CW-NA-CN", "K_q": 70.0, "qeq": 111.60},
        {"bind": "H-NA-CN ", "K_q": 30.0, "qeq": 123.10},
        {"bind": "CK-NB-CB", "K_q": 70.0, "qeq": 103.80},
        {"bind": "CR-NB-CC", "K_q": 70.0, "qeq": 117.00},
        {"bind": "CV-NB-CR", "K_q": 70.0, "qeq": 117.00},
        {"bind": "CA-NC-C", "K_q": 70.0, "qeq": 120.50},
        {"bind": "CB-NC-CA", "K_q": 70.0, "qeq": 112.20},
        {"bind": "CQ-NC-CA", "K_q": 70.0, "qeq": 118.60},
        {"bind": "CQ-NC-CB", "K_q": 70.0, "qeq": 111.00},
        {"bind": "HO-OH-C", "K_q": 35.0, "qeq": 113.00},
        {"bind": "HO-OH-CT", "K_q": 55.0, "qeq": 108.50},
        {"bind": "P-OH-HO", "K_q": 45.0, "qeq": 108.50},
        {"bind": "CT-OS-CT", "K_q": 60.0, "qeq": 109.50},
        {"bind": "P-OS-CT", "K_q": 100.0, "qeq": 120.50},
        {"bind": "P-OS-P ", "K_q": 100.0, "qeq": 120.50},
        {"bind": "OH-P-O2", "K_q": 45.0, "qeq": 108.23},
        {"bind": "O2-P-O2", "K_q": 140.0, "qeq": 119.90},
        {"bind": "OS-P-O2", "K_q": 100.0, "qeq": 108.23},
        {"bind": "OS-P-OH", "K_q": 45.0, "qeq": 102.60},
        {"bind": "OS-P-OS", "K_q": 45.0, "qeq": 102.60},
        {"bind": "CT-S-CT", "K_q": 62.0, "qeq": 98.90},
        {"bind": "S-S-CT", "K_q": 68.0, "qeq": 103.70},
        {"bind": "HS-SH-CT", "K_q": 43.0, "qeq": 96.00},
        {"bind": "HS-SH-HS", "K_q": 35.0, "qeq": 92.07},
        {"bind": "F-CT-F ", "K_q": 77.0, "qeq": 109.10},
        {"bind": "H1-CT-F", "K_q": 35.0, "qeq": 109.50}
    ]
}

__van_der_waals_params = {
    "data": [
        {"bind": "H ", "R*j": 0.6000, "e_k": 0.0157},
        {"bind": "HO", "R*j": 0.0000, "e_k": 0.0000},
        {"bind": "HS", "R*j": 0.6000, "e_k": 0.0157},
        {"bind": "HC", "R*j": 1.4870, "e_k": 0.0157},
        {"bind": "H1", "R*j": 1.3870, "e_k": 0.0157},
        {"bind": "H2", "R*j": 1.2870, "e_k": 0.0157},
        {"bind": "H3", "R*j": 1.1870, "e_k": 0.0157},
        {"bind": "HP", "R*j": 1.1000, "e_k": 0.0157},
        {"bind": "HA", "R*j": 1.4590, "e_k": 0.0150},
        {"bind": "H4", "R*j": 1.4090, "e_k": 0.0150},
        {"bind": "H5", "R*j": 1.3590, "e_k": 0.0150},
        {"bind": "HW", "R*j": 0.0000, "e_k": 0.0000},
        {"bind": "O ", "R*j": 1.6612, "e_k": 0.2100},
        {"bind": "O2", "R*j": 1.6612, "e_k": 0.2100},
        {"bind": "OW", "R*j": 1.7682, "e_k": 0.1521},
        {"bind": "OH", "R*j": 1.7210, "e_k": 0.2104},
        {"bind": "OS", "R*j": 1.6837, "e_k": 0.1700},
        {"bind": "CT", "R*j": 1.9080, "e_k": 0.1094},
        {"bind": "C ", "R*j": 1.9080, "e_k": 0.0860},
        {"bind": "N ", "R*j": 1.8240, "e_k": 0.1700},
        {"bind": "N3", "R*j": 1.8240, "e_k": 0.1700},
        {"bind": "S ", "R*j": 2.0000, "e_k": 0.2500},
        {"bind": "SH", "R*j": 2.0000, "e_k": 0.2500},
        {"bind": "P ", "R*j": 2.1000, "e_k": 0.2000},
        {"bind": "IM", "R*j": 2.47, "e_k": 0.1},
        {"bind": "Li", "R*j": 1.1370, "e_k": 0.0183},
        {"bind": "IP", "R*j": 1.8680, "e_k": 0.00277},
        {"bind": "K ", "R*j": 2.6580, "e_k": 0.000328},
        {"bind": "Rb", "R*j": 2.9560, "e_k": 0.00017},
        {"bind": "Cs", "R*j": 3.3950, "e_k": 0.0000806},
        {"bind": "I ", "R*j": 2.35, "e_k": 0.40},
        {"bind": "F ", "R*j": 1.75, "e_k": 0.061},
        {"bind": "IB", "R*j": 5.0, "e_k": 0.1},
        {"bind": "EP", "R*j": 0.0, "e_k": 0.0},
    ]
}

bending_energy = process_energy(__bending_energy)
bs_energy = process_energy(__bs_energy)
vdw_params = process_energy(__van_der_waals_params)

vdw_params_Rj_mean = Rj_mean(__van_der_waals_params)
vdw_params_ek_mean = ek_mean(__van_der_waals_params)
bs_energy_K_r_mean = K_r_mean(__bs_energy)
bs_energy_req_mean = req_mean(__bs_energy)
bending_energy_K_q_mean = K_q_mean(__bending_energy)
bending_energy_qeq_mean = qeq_mean(__bending_energy)
