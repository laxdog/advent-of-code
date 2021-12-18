#!/usr/bin/env python3

def get_lines(file_type=0):
    if file_type==0:
        return parse_file('input')
    else:
        return parse_file(f'sample{file_type}')

def parse_file(file):
    with open(file, 'r') as f:
        chars =  [[x for x in line.strip()] for line in f.readlines() if line.strip()][0]
        binary = ""
        for char in chars:
            binary += bin(int(char, 16))[2:].zfill(4)
    return binary
        

def parse_data(data, ver_sum=0, num_pack=99999):
    print(f"Entered loop with {data}, len {len(data)}")
    cur = 0
    pack_cnt = 0
    while cur < len(data) and num_pack != pack_cnt:
        pack_cnt += 1
        print(f"Cursor at {cur} data len {len(data)}")
        _ver = data[cur:cur+3]
        ver = int(_ver, 2)
        ver_sum += ver
        cur += 3
        _tid = data[cur:cur+3]
        tid = int(_tid, 2)
        cur += 3
        print(f"Ver: {ver}, TID: {tid}, Ver: {_ver}, TID: {_tid}")
        if tid == 4:
            _bits = ""
            leading = None
            while leading != "0":
                leading = data[cur]
                cur += 1
                _bits += data[cur:cur+4]
                cur += 4
            print(f"Lead: {leading}, Num: {int(_bits, 2)}, Bits: {_bits}, Cursor at {cur} data len {len(data)}")
        else:
            ltid = data[cur]
            cur += 1
            if ltid == "0":
                _tot_len = data[cur:cur+15]
                cur += 15
                if not _tot_len:
                    import ipdb; ipdb.set_trace()
                tot_len = int(_tot_len, 2)
                _ver_sum, cur = parse_data(data[cur:cur+tot_len], ver_sum)
                ver_sum += _ver_sum
                assert cur == tot_len
                return ver_sum, cur
            else:
                _num_sub = data[cur:cur+11]
                num_sub = int(_num_sub, 2)
                cur += 11
                _ver_sum, cur = parse_data(data[cur:], ver_sum,  num_pack=num_sub)
                ver_sum += _ver_sum
                return ver_sum, cur
        if set(data[cur:]) == {"0"}:
            cur = len(data)
    return ver_sum, cur

for i in range(1, 8):
    print("-="*15, "Sample", i, "-="*15)
    data = get_lines(i)
    print(f"VerSum: {parse_data(data)}")
    print("-="*40)