import logging

logging.basicConfig(filename="lists.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


class Lists:
    logging.info("Accessing List class...")

    def extract_list(self, l):
        self.l = l
        """ This function extracts all the list entity """
        logging.info("Entered the extract_list function...")
        try:
            for i in self.l:
                if type(i) == list:
                    return i
        except Exception as e:
            logging.exception("Exception Occurred!")
            return e
        finally:
            logging.info("Exiting function...")

    def find_numericals(self, l):
        self.l = l
        """ This function extracts all the numerical data (it may be a part of dict key and values) """
        logging.info("Entered find_numerical function")
        try:
            new_list = []
            for i in self.l:
                for j in i:
                    if type(j) == int:
                        new_list.append(j)
                if type(i) == dict:
                    for n, m in i.items():
                        if type(n) == int or type(m) == int:
                            new_list.append(n)
                            new_list.append(m)

            return new_list
        except Exception as e:
            logging.exception("Error Occurred!")
            return e
        finally:
            logging.info("Exiting function...")

    def extract_ineuron(self, l):
        self.l = l
        """This function extracts 'ineuron' out of given data"""
        logging.info("Entered extract_ineuron function")
        try:
            found = False
            for i in self.l:
                if type(i) == list:
                    logging.info("Inside list...")
                    for j in i:
                        if j == 'ineuron':
                            logging.info("Found...")
                            found = True
                if type(i) == dict:
                    logging.info("Inside dict...")
                    for m in i.values():
                        if m == 'ineuron':
                            logging.info("Found...")
                            found = True
            if found == True:
                return "ineuron"
        except Exception as e:
            logging.exception("Exception occurred...")
            return e
        finally:
            logging.info("Exiting extract_ineuron function...")

    def flat_list(self, l):
        self.l = l
        """ This function unwrap all the collection inside collection and create a flat list """
        logging.info("Entered flat_list function..")
        try:
            new_list = []
            for i in self.l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        new_list.append(j)
                if type(i) == dict:
                    for m, n in i.items():
                        new_list.append(m)
                        new_list.append(n)

            return new_list
        except Exception as e:
            logging.exception("Exception Occurred...")
            return e
        finally:
            logging.info("Quitting function")


# Testing ...
sample_data = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), {23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5}, {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]

r = 12345

li = Lists()
print(li.extract_list(sample_data))
print(li.find_numericals(sample_data))
print("found:", li.extract_ineuron(sample_data))
print(li.flat_list(r))
print(li.flat_list(sample_data))

