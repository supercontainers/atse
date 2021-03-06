#!/usr/bin/python

import sys
import re
import os
import time
import subprocess
import argparse

# Get 1 sample of tx2mon output
cmd = "tx2mon -q -t -d .0001 -f /dev/stdout"
result = subprocess.check_output(cmd, shell=True)

# Parse the sample
result = result.splitlines()
fields = re.split(',', result[1])

# Secret decoder ring
#timestamp,                  0
#cpu_temp0c0,                1
#cpu_freq0c0,                2
#cpu_temp0c1,                3
#cpu_freq0c1,                4
#cpu_temp0c2,                5
#cpu_freq0c2,                6
#cpu_temp0c3,                7
#cpu_freq0c3,                8
#cpu_temp0c4,                9
#cpu_freq0c4,                10
#cpu_temp0c5,                11
#cpu_freq0c5,                12
#cpu_temp0c6,                13
#cpu_freq0c6,                14
#cpu_temp0c7,                15
#cpu_freq0c7,                16
#cpu_temp0c8,                17
#cpu_freq0c8,                18
#cpu_temp0c9,                19
#cpu_freq0c9,                20
#cpu_temp0c10,               21
#cpu_freq0c10,               22
#cpu_temp0c11,               23
#cpu_freq0c11,               24
#cpu_temp0c12,               25
#cpu_freq0c12,               26
#cpu_temp0c13,               27
#cpu_freq0c13,               28
#cpu_temp0c14,               29
#cpu_freq0c14,               30
#cpu_temp0c15,               31
#cpu_freq0c15,               32
#cpu_temp0c16,               33
#cpu_freq0c16,               34
#cpu_temp0c17,               35
#cpu_freq0c17,               36
#cpu_temp0c18,               37
#cpu_freq0c18,               38
#cpu_temp0c19,               39
#cpu_freq0c19,               40
#cpu_temp0c20,               41
#cpu_freq0c20,               42
#cpu_temp0c21,               43
#cpu_freq0c21,               44
#cpu_temp0c22,               45
#cpu_freq0c22,               46
#cpu_temp0c23,               47
#cpu_freq0c23,               48
#cpu_temp0c24,               49
#cpu_freq0c24,               50
#cpu_temp0c25,               51
#cpu_freq0c25,               52
#cpu_temp0c26,               53
#cpu_freq0c26,               54
#cpu_temp0c27,               55
#cpu_freq0c27,               56
#tmon_soc_avg0,              57
#freq_mem_net0,              58
#v_core0,                    59
#v_sram0,                    60
#v_mem0,                     61
#v_soc0,                     62
#pwr_core0,                  63
#pwr_sram0,                  64
#pwr_mem0,                   65
#pwr_soc0,                   66
#thrott_cause0,              67
#temp_thrott_cnt0,           68
#pwr_thrott_cnt0,            69
#ext_thrott_cnt0,            70
#temp_thrott_dur0,           71
#pwr_thrott_dur0,            72
#ext_thrott_dur0,            73
#
#cpu_temp1c0,                74
#cpu_freq1c0,                75
#cpu_temp1c1,                76
#cpu_freq1c1,                77
#cpu_temp1c2,                78
#cpu_freq1c2,                79
#cpu_temp1c3,                80
#cpu_freq1c3,                81
#cpu_temp1c4,                82
#cpu_freq1c4,                83
#cpu_temp1c5,                84
#cpu_freq1c5,                85
#cpu_temp1c6,                86
#cpu_freq1c6,                87
#cpu_temp1c7,                88
#cpu_freq1c7,                89
#cpu_temp1c8,                90
#cpu_freq1c8,                91
#cpu_temp1c9,                92
#cpu_freq1c9,                93
#cpu_temp1c10,               94
#cpu_freq1c10,               95
#cpu_temp1c11,               96
#cpu_freq1c11,               97
#cpu_temp1c12,               98
#cpu_freq1c12,               99
#cpu_temp1c13,               100
#cpu_freq1c13,               101
#cpu_temp1c14,               102
#cpu_freq1c14,               103
#cpu_temp1c15,               104
#cpu_freq1c15,               105
#cpu_temp1c16,               106
#cpu_freq1c16,               107
#cpu_temp1c17,               108
#cpu_freq1c17,               109
#cpu_temp1c18,               110
#cpu_freq1c18,               111
#cpu_temp1c19,               112
#cpu_freq1c19,               113
#cpu_temp1c20,               114
#cpu_freq1c20,               115
#cpu_temp1c21,               116
#cpu_freq1c21,               117
#cpu_temp1c22,               118
#cpu_freq1c22,               119
#cpu_temp1c23,               120
#cpu_freq1c23,               121
#cpu_temp1c24,               122
#cpu_freq1c24,               123
#cpu_temp1c25,               124
#cpu_freq1c25,               125
#cpu_temp1c26,               126
#cpu_freq1c26,               127
#cpu_temp1c27,               128
#cpu_freq1c27,               129
#tmon_soc_avg1,              130
#freq_mem_net1,              131
#v_core1,                    132
#v_sram1,                    133
#v_mem1,                     134
#v_soc1,                     135
#pwr_core1,                  136
#pwr_sram1,                  137
#pwr_mem1,                   138
#pwr_soc1,                   139
#thrott_cause1,              140
#temp_thrott_cnt1,           141
#pwr_thrott_cnt1,            142
#ext_thrott_cnt1,            143
#temp_thrott_dur1,           144
#pwr_thrott_dur1,            145
#ext_thrott_dur1             146

print fields
