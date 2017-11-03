import random, sys
import time
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    '''
    Main class that will run the herd immunity simulation program.  Expects initialization
    parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.

    _____Attributes______

    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.

    population_size: Int.  The size of the population for this simulation.

    population: [Person].  A list of person objects representing all people in
        the population.

    next_person_id: Int.  The next available id value for all created person objects.
        Each person should have a unique _id value.

    virus_name: String.  The name of the virus for the simulation.  This will be passed
    to the Virus object upon instantiation.

    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.

    basic_repro_num: Float between 0 and 1.   This will be passed
    to the Virus object upon instantiation.

    vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
        vaccinated for the given simulation.

    current_infected: Int.  The number of currently people in the population currently
        infected with the disease in the simulation.

    total_infected: Int.  The running total of people that have been infected since the
    simulation began, including any people currently infected.

    total_dead: Int.  The number of people that have died as a result of the infection
        during this simulation.  Starts at zero.


    _____Methods_____

    __init__(population_size, vacc_percentage, virus_name, mortality_rate,
     basic_repro_num, initial_infected=1):
        -- All arguments will be passed as command-line arguments when the file is run.
        -- After setting values for attributes, calls self._create_population() in order
            to create the population array that will be used for this simulation.

    _create_population(self, initial_infected):
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
    '''

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.virus = Virus(virus_name, mortality_rate, basic_repro_num)

        # Evenually chave the name change 
        self.logger = Logger('simulation')
        # This attribute will be used to keep track of all the people that catch
        # the infection during a given time step. We'll store each newly infected
        # person's .ID attribute in here.  At the end of each time step, we'll call
        # self._infect_newly_infected() and then reset .newly_infected back to an empty
        # list.

        # new infected person, by id// Used newly infected to add to infetced
        self.newly_infected = []
        #Create a population
        self._create_population(initial_infected, vacc_percentage)

    def _create_population(self, initial_infected, vacc_percentage):
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        population = []
        infected_count = 0
        while len(population) != pop_size:
            self.next_person_id +=1
            if infected_count !=  initial_infected:
                population.append(Person(self.next_person_id, False, self.virus))
                infected_count +=1 
                self.total_infected +=1
            else:
                if random.uniform(0,1) > vacc_percentage:
                    population.append(Person(self.next_person_id, True,self.virus))
                    self.total_infected +=1
                else:
                    population.append(Person(self.next_person_id, False, None))
        self.population = population
        print("start total inf: {}".format(self.total_infected))
        time.sleep(2)

    #Check to see if all are dead or there are no infected people
    def _simulation_should_continue(self):
        if all(person.is_alive == False for person in self.population):
            print("everyone is dead")
            return False
        if self.total_infected == len(self.population):
            return False
        else:
            return True
            
    def run(self):
        # TODO: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0

        should_continue = self._simulation_should_continue()
        while should_continue:
        # adding one to counter and running one itteration
            print("alive ppl {}".format(len([person for person in self.population if person.is_alive ==True])))
            time_step_counter +=1
            self.time_step()
        # round of this simulation.  At the end of each iteration of this loop, remember
        # to rebind should_continue to another call of self._simulation_should_continue()!
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        # TODO: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population:
            #        - Repeat for 100 total interactions:
            #             - Grab a random person from the population.
            #           - If the person is dead, continue and grab another new
            #                 person from the population. Since we don't interact
            #                 with dead people, this does not count as an interaction.
            #           - Else:
            #               - Call simulation.interaction(person, random_person)
            #               - Increment interaction counter by 1.
        time.sleep(2)
        sick_pop = [person for person in self.population if person.infected]
        print(len(sick_pop))
        for sick_person in sick_pop:
            if sick_person.is_alive:
                interaction_cnt=0
                while interaction_cnt <100:
                    rand_person = random.choice(self.population)
                    if rand_person.is_alive == True:
                        interaction_cnt +=1
                        #Log these
                        #print("1:{} 2:{}".format(sick_person._id, rand_person._id))
                        print('interaction num{} between {} and {}'.format(interaction_cnt, sick_person._id, rand_person._id))
                        self.interaction(sick_person, rand_person)
                    else:
                        rand_person = random.choice(self.population)
                self._infect_newly_infected()
            if sick_person.did_survive_infection():
                self.total_infected -=1


    # An interaction between a sick person and a random person who is alive
    def interaction(self, person, random_person):

        if random_person.is_vaccinated == True or random_person.infected !=None:
            pass
        else:
            if (self.virus.get_repo_rate() <random.uniform(0,1)):
                print("{} is now sick.".format(random_person._id))
                self.total_infected +=1
                self.newly_infected.append(random_person._id)
        # log the interaction in the future



    #sets person in population to sick based on id
    def _infect_newly_infected(self):
        for _id in self.newly_infected:
            for person in self.population:
                if person._id == _id:
                    person.infected = self.virus
        self.newly_infected = []

if __name__ == "__main__":
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
