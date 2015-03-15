__author__ = 'Soheil'
import subprocess
import re


def ping(host='google.com', alias=None, number_of_packets=4, verbosity=0):
    try:
        ping_excec = subprocess.Popen(["ping", "-n", str(number_of_packets), host], stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
        out, error = ping_excec.communicate()

        if out:
            if verbosity == 2:
                print(out)
            try:
                minimum = int(re.findall(r"Minimum = (\d+)", out)[0])
                maximum = int(re.findall(r"Maximum = (\d+)", out)[0])
                average = int(re.findall(r"Average = (\d+)", out)[0])
                loss = int(re.findall(r"Lost = (\d+)", out)[0])
                result = PingResult(host, alias, minimum, maximum, average, number_of_packets, loss)
                if verbosity == 1:
                    print(result)
                return result
            except Exception as exc:
                print "no data for one of minimum, maximum, average, loss: {}".format(exc)
        else:
            print 'No ping'

    except Exception as exc:
        print ('EXCEPTION: {}'.format(exc))


class PingResult():
    def __init__(self, host, alias, minimum, maximum, average, packets, lost):
        self.host = host
        self.alias = alias
        self.minimum = minimum
        self.maximum = maximum
        self.average = average
        self.lost = lost
        self.packets = packets
        self.lost_percentage = lost / packets * 100

    def __str__(self):
        return '\nPing on {} ({})\nPackets: {}    Min: {}    Max: {}    Average= {}    Loss: {} ({}%)'.format(self.host, self.alias,
                                                                                                        self.packets,
                                                                                                        self.minimum,
                                                                                                        self.maximum,
                                                                                                        self.average,
                                                                                                        self.lost,
                                                                                                        self.lost_percentage)