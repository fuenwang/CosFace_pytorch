import os

if __name__ == '__main__':
    path = '/home/t-fuenwang/Data/CASIA-WebFace_116x100'
    out = './casia_list.txt'

    people_lst = [x for x in sorted(os.listdir(path)) if os.path.isdir('%s/%s'%(path, x))]
    data = []
    for idx, person in enumerate(people_lst):
        person_path = '%s/%s'%(path, person)
        img_lst = [x for x in sorted(os.listdir(person_path)) if x.endswith('.jpg')]
        tmp = [('%s/%s'%(person, x), idx) for x in img_lst]
        data += tmp

    with open(out, 'w') as f:
        for one in data:
            s = '%s %d'%(*one,)
            f.write(s + '\n')
