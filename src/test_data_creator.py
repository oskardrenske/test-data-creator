from loguru import logger
import jsonlines


from src.utils import (
    create_phone_number,
    random_true_false,
    street_number,
    get_random_from_list,
    timestamp,
    combine_prefix_suffix,
    load_data_from_file,
    create_dir,
    old_date,
    number_of_persons,
    pretty_print,
)


class TestDataCreator:
    def __init__(self):
        self.personnummer = load_data_from_file(filename="personnummer.txt")
        self.first_names = load_data_from_file("first_names.txt")
        self.last_names = load_data_from_file("last_names.txt")
        self.addresses = self.create_addresses()
        self.postnr_ort = load_data_from_file("postnummer_ort.txt")
        self.total = 0
        self.result = []
        self.output_filename = f"test_data_{timestamp()}.jsonl"
        self.output_dir = create_dir("output")
        self.output_full_path = self.output_dir / self.output_filename
        self.number_of_persons = number_of_persons()

    def create_addresses(self) -> list:
        """
        Combine address rpefix with address suffix
        Some suffixes are more common and have several entries in the text file
        """
        address_prefix = load_data_from_file("address_prefix.txt")
        address_suffix = load_data_from_file("address_suffix.txt")
        return combine_prefix_suffix(prefixes=address_prefix, suffixes=address_suffix)

    def write_person_to_file(self, person):
        with jsonlines.open(self.output_full_path, mode="a") as f:
            f.write(person)

    def get_unique_personnummer(self) -> dict:
        pnr_left_in_list = len(self.personnummer)
        if pnr_left_in_list == 0:
            logger.warning("No personnummer left")
            return {"personnummer": 0, "remaining": False}
        pnr = get_random_from_list(self.personnummer)
        self.personnummer.remove(pnr)
        return {"personnummer": pnr, "remaining": True}

    def create_person(self, person_nr):
        return {
            "personnummer": person_nr,
            "first_name": get_random_from_list(self.first_names),
            "last_name": get_random_from_list(self.last_names),
            "adress": get_random_from_list(self.addresses).capitalize(),
            "gatunummer": street_number(),
            "postnummer_ort": get_random_from_list(self.postnr_ort),
            "phone": create_phone_number(),
            "active": random_true_false(),
            "start_date": old_date(),
        }

    def create_test_data(self):
        logger.info(f"Create test data for {self.number_of_persons} persons")
        total = 0
        for i in range(self.number_of_persons):
            result = self.get_unique_personnummer()
            if not result["remaining"]:
                break

            person = self.create_person(result["personnummer"])
            self.write_person_to_file(person)
            pretty_print(person)
            total += 1
        logger.info(f"Wrote test data for {total} persons to '{self.output_full_path}'")
