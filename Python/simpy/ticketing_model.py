import simpy
class Ticket(object):
    def __init__(self, env):
         self.env = env
         self.action = env.process(self.run())
    def run(self):
        while True:
            print('Start collecting requests at %d' % self.env.now)
            requesting_duration = 5
            # We may get interrupted while the ticketing process is ongoing
            try:
                yield self.env.process(self.request(requesting_duration))
            except simpy.Interrupt:
                # When we received an interrupt, we stop ticketing and
                # switch to the break state
                print('We have stopped for lunch break at %d and will resume after 3 unit break.' % self.env.now)
                break_duration = 3
                yield self.env.process(self.request(break_duration))
                print('Now resuming work at %d' % self.env.now)
            print('Start ticketing at %d' % self.env.now)
            ticketing_duration = 5
            yield self.env.timeout(ticketing_duration)

    def request(self, duration):
        yield self.env.timeout(duration)



def driver(env, ticket):
    yield env.timeout(15)
    ticket.action.interrupt()

env = simpy.Environment()
ticket = Ticket(env)
env.process(driver(env, ticket))
env.run(until=35)
