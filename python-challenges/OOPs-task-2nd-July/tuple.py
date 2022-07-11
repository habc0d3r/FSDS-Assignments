import logging
logging.basicConfig(filename="tuple.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class Tuples():
    logging.info("Accessing Tuple class.")

    def extract_tuple(self, l):
        """ This function extracts all the tuple entity """
        self.l = l
        logging.info("Entered extract_tuple function...")
        try:
            t = []
            for i in self.l:
                if type(i) == tuple:
                    t.append(i)
            return t
        except Exception as e:
            logging.exception("Exception occurred..")
            return e
        finally:
            logging.info("Exiting function...")


# Testing ...
sample_data = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5}, {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

tup = Tuples()
print(tup.extract_tuple(sample_data))
