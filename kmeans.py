import numpy as np
import matplotlib.pyplot as plt
import math
import random
np.random.seed(1)


def create_points(numer_of_points):
    a = np.random.randint(0, 100, size=numer_of_points)
    b = np.random.randint(0, 100, size=numer_of_points)
    return list(zip(a, b))


def calculate_distace(a, b):
    d = math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return d


def create_centroids(n):
    centroid_list = []
    for _ in range(n):
        centroid = (np.random.randint(0, 100), np.random.randint(0, 100))
        centroid_list.append(centroid)
    return centroid_list


def assign_centroids(points, centroids):
    assigned_points = {centroid: [] for centroid in centroids}
    for point in points:
        distances = {}
        for centroid in centroids:
            distances[centroid] = calculate_distace(centroid, point)
        closest_centroid = min(distances, key=distances.get)
        assigned_points[closest_centroid].append(point)
    return assigned_points


def plot_points(categorized_points):
    colors = ["#" + ''.join([random.choice('0123456789ABCDEF')
                            for i in range(6)]) for c in range(len(categorized_points))]
    i = 0
    for centroid in categorized_points:
        color = colors[i]
        plt.scatter(centroid[0], centroid[1], marker="*", s=200, c=color)
        for point in categorized_points[centroid]:

            plt.scatter(point[0], point[1], c=color)
        i += 1


def adjust_centroids(categorized_points):
    new_centroids = []
    for centroid in categorized_points:
        if len(categorized_points[centroid]) > 0:
            x, y = 0, 0
            for point in categorized_points[centroid]:
                x = x+point[0]
                y = y+point[1]
            x = x/len(categorized_points[centroid])
            y = y/len(categorized_points[centroid])
            new_centroids.append((x, y))
        else:
            new_centroids.append(centroid)
    return new_centroids


def kmeans(points, iterations, categorized_points=None, steps=None):
    if categorized_points == None:
        categorized_points = assign_centroids(points, centroids)
        steps = 0
    if iterations == 0:
        return categorized_points
    else:
        new_centroids = adjust_centroids(categorized_points)
        centroid_list = list(categorized_points.keys())
        distances = []
        for i in range(len(centroid_list)):
            distance = calculate_distace(centroid_list[i], new_centroids[i])
            distances.append(distance)
        stop = True
        for distance in distances:
            if distance > 0.1:
                stop = False
                break
        if stop:
            print("Completed after "+str(steps)+" steps")
            return categorized_points
        steps += 1

        new_cat_points = assign_centroids(points, new_centroids)
        return kmeans(points, iterations-1, new_cat_points, steps)


points = create_points(200)
centroids = create_centroids(6)

new_cat_points = kmeans(points, 100)

plot_points(new_cat_points)

plt.show()
