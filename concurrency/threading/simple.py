import concurrent.futures
import threading
import time

start = time.perf_counter()


def do_something(seconds=1):
    print(f"Sleeping {seconds} second(s)..")
    time.sleep(seconds)
    print(f"Done sleeping for {seconds}")


def main():
    ####################################
    # t1 = threading.Thread(target=do_something)
    # t2 = threading.Thread(target=do_something)

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()
    ####################################

    ####################################
    # threads = []
    # for _ in range(10):
    #     t = threading.Thread(target=do_something, args=[1.5])
    #     t.start()
    #     threads.append(t)

    # for thread in threads:
    #     thread.join()
    ####################################

    #########################
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #     secs = [5, 4, 3, 2, 1]
    #     all_futures = [executor.submit(do_something, sec) for sec in secs]

    #     for f in concurrent.futures.as_completed(all_futures):
    #         print(f.result())
    #########################
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")


if __name__ == "__main__":
    main()
