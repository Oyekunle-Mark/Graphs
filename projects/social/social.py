from random import shuffle
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        # loop over a range of 0 to numUsers
        for i in range(0, numUsers):
            # add user to the graph
            self.addUser(f"User {i}")

        # create friendships

        # Generate all friendship combinations
        # make a list of possible friendships
        possibleFriendships = []
        # avoid duplicates ensuring that the first number is smaller than the second

        # loop over userID in users
        for userID in self.users:
            # loop over friend id in a range from user id + 1 to the lastID +1
            for friendID in range(userID + 1, self.lastID + 1):
                # append the tuple of (user id , friend id) to the possible friendships list
                possibleFriendships.append((userID, friendID))

        # shuffle the possible friendships using the random.shuffle method
        shuffle(possibleFriendships)

        # create a friendship of the first x amount of pairs in the list
        # X determined by the formula: numUsers * avgFriendships // 2
        # we need to divide by two as each createFriendship adds 2 friendships
        # loop over a range to numUsers * avgFriendships // 2
        for i in range(numUsers * avgFriendships // 2):
            # set the friendship to possible friends at i
            friendship = possibleFriendships[i]
            # addfriendship of friendship[0] and friendship[1]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # create a queue
        q = Queue()
        # enqueue a list holding the starting userID
        q.enqueue([userID])
        # created an empty visited dictionary
        visited = {}  # Note that this is a dictionary, not a set

        # counts up the number of separations between userID and other nodes
        separation = 0

        # while the queue is not empty
        while q.size() > 0:
            # dequeue to the path
            path = q.dequeue()
            # set a user to the last item in the path
            user = path[-1]
            # if user is not in visited
            if user not in visited:
                # add user to visited dictionary
                visited[user] = path
                # increment separation by len of path
                separation += len(path)

                # loop over next users in friendships at the index of user
                for next_user in self.friendships[user]:
                    # set a new path equal to a new list of the path (copy)
                    new_path = list(path)
                    # append next user to new path
                    new_path.append(next_user)
                    # enqueue the new path
                    q.enqueue(new_path)

        # print out some relevant stats
        print("")
        print('****** Average degree of separation',
              separation // len(visited), "******")
        print(
            f"****** Percentage of other users in user {userID} extended network", len(visited) / len(self.friendships) * 100, "******")

        # return visited
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)

    print("\nThe social graph:")
    print(sg.friendships)

    userID = 1
    connections = sg.getAllSocialPaths(userID)

    print(f"\nUser {userID} connections and path:")
    print(connections)
