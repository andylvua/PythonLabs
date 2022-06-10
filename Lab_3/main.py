import log_parser as lp


def main():
    lp.statistics_of_requests_in_datetime_range(file_path="resources/access_log.zip",
                                                start_datetime="08/Mar/2004:05:10:27",
                                                end_datetime="12/Mar/2004:16:21:50",
                                                save_plot=True)


if __name__ == "__main__":
    main()
