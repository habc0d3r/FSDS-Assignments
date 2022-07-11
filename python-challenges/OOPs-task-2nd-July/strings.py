import logging
logging.basicConfig(filename="strings.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class Strings():
    logging.info("Accessing Strings class.")

    def extract_str(self, l):
        """ This function extracts all the string entities """
        self.l = l
        logging.info("Entered extract_str function...")
        try:
            all_str = []
            for i in self.l:
                if type(i) == dict:
                    for j, k in i.items():
                        if type(j) == str or type(k) == str:
                            all_str.append(j)
                            all_str.append(k)
            for m in i:
                if type(m) == str:
                    all_str.append(m)
            return all_str
        except Exception as e:
            logging.exception("Exception Occurred...")
            return e
        finally:
            logging.info("Exiting function...")


# Testing ...
sample_data = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5}, {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

string = Strings()
print(string.extract_str(sample_data))