import random
from util import Queue, Stack

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # Add users
        # iterate over 0 to num users...
        for i in range(0, num_users):
            # add user using an f-string
            self.add_user(f'User {i}')

        # Create friendships
        # generate all possible friendship combinations
        possible_friendships = []

        # avoid dups by making sure the first number is smaller than the second
        # iterate over user id in users...
        for user_id in self.users:
            # iterate over friend id in in a range from user id + 1 to last id + 1...
            for friend_id in range(user_id+1, self.last_id+1):
                # append a user id and friend id tuple to the possible friendships
                possible_friendships.append((user_id, friend_id))
        
        # shuffle friendships random import
        random.shuffle(possible_friendships)

        # create friendships for the first N pairs of the list
        # N is determined by the formula: num users * avg friendships // 2
        # NOTE: need to divide by 2 since each add_friendship() creates 2 friendships
        # iterate over a range using the formula as the end base...
        for i in range(num_users * avg_friendships // 2):
            # set friendship to possible friendships at index
            friendships = possible_friendships[i]
            # add friendship of frienship[0], friendship[1]
            self.add_friendship(friendships[0], friendships[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        # Create an empty queue and enqueue A PATH TO the user id 
        q = Queue()
        q.enqueue([user_id])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH eg -> [a, b, c, r, g]
            path = q.dequeue()
            # Grab the current from the last item in PATH
            current_friend = path[-1]
            # loop over each friend in the friendships at the current friend
            for friend in self.friendships[current_friend]:
                # if the friend is not in visited
                if friend not in visited:
                    visited[friend] = path
                    # copy the path that we used in order to get to this friend
                    new_path = list(path)
                    # append the next friend accosiated with the friend to the new path
                    new_path.append(friend)
                    # Store the list in the Queue and reloop
                    q.enqueue(new_path)

               # For all of the vertices acosiated with the vertex Then add A PATH TO its neighbors to the back of the queue

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
