from Dictionary import dictionary

def main():
    print("main")
    d = dictionary.get_personal_data()
    print(dictionary.get_personal_data())
    for key in sorted(d.keys()):
        print("%s: %s" % (key, d[key]))

if __name__ == "__main__":
    main()