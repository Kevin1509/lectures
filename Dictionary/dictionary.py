def get_personal_data():
    """Return a dictionary of personal information"""
    print("")
    personal_data = {"name": "Jim", "role": "teacher"}
    return personal_data

def main() -> int:
    some_dict = dict()
    initialized_dict = dict([('name','Jim'),('a_role', 'joker')])
    simple_init_dict = dict(name='Jim', a_role='teacher')
    print(some_dict)
    print(initialized_dict)
    print(simple_init_dict)
    simple_init_dict['a_role'] = 'joker'
    print(simple_init_dict)

    my_compression = {x: x**2 for x in range(5)}
    print(my_compression)

    s = "little,".translate({ord(i): None for i in string.punctuation})
    print(s)



    return 0


if __name__=='__main__':
    main()