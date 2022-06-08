import log_parser as lp


def main():
    lp.statistics_of_requests_in_datetime_range("resources/access_log.zip",
                                                "08/Mar/2004:05:10:27",
                                                "12/Mar/2004:16:21:50")


if __name__ == "__main__":
    main()
