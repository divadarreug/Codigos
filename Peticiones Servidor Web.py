import unittest
import concurrent.futures
import requests

class ConcurrentTests(unittest.TestCase):
    def test_concurrent(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            # Crea una lista de futuros para realizar solicitudes concurrentes
            futures = [executor.submit(requests.get, 'https://vecinosenaccion-riobamba.com/') for i in range(1000)]

            # Espera hasta que todas las solicitudes se completen
            concurrent.futures.wait(futures)

            # Crea un archivo de informe de texto
            with open('War_Concurrencia.txt', 'w') as report:
                for future in futures:
                    result = future.result()
                    if result.status_code == 200:
                        report.write("Request {} succeeded with status code {}\n".format(future, result.status_code))
                    else:
                        report.write("Request {} failed with status code {}\n".format(future, result.status_code))
                        self.fail("Request {} failed with status code {}".format(future, result.status_code))

if __name__ == '__main__':
    unittest.main()