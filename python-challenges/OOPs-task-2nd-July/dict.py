import logging
logging.basicConfig(filename="dict.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class Dictionary:
    logging.info("Accessing Dictionary class...")

    def extract_dict(self, l):
        self.l = l
        """ This function extracts all the dict entities """
        logging.info("Entered extract_dict function...")
        try:
            for i in self.l:
                if type(i) == dict:
                    return i
        except Exception as e:
            logging.exception("Exception Occurred...")
            return e
        finally:
            logging.info("Exiting function...")

    def num_keys(self, l):
        self.l = l
        """ This function finds out number of keys in dict element """
        logging.info("Entered num_keys function...")
        try:
            for i in self.l:
                if type(i) == dict:
                    return len(list(i.keys()))
        except Exception as e:
            logging.exception("Exception Occurred...")
            return e
        finally:
            logging.info("Exiting function...")


# Testing ...
sample_data = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5}, {'k1': "sudh", "k2": "inueron", "k3": "kumar", 3: 6, 7: 8}, ["inueron", "data science"]]
r = 3434

d = Dictionary()
print(d.num_keys(sample_data))
print(d.extract_dict(r))

