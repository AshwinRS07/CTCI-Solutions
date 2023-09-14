# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.

# Example of input : projects = [[0,1],[1,2],[1,3],[0,2]]

# Create an adjacency list where {project -> dependencies}, iterate till all projects are built or we can't add any more projects

def build_order(projects):
    dependency_list = {}
    for dependency, project in projects:
        if project not in dependency_list:
            dependency_list[project] = []
        if dependency not in dependency_list:
            dependency_list[dependency] = []
        dependency_list[project].append(dependency)
    print(dependency_list)
    num_projects = len(dependency_list)
    build_order = []
    length_last = 0
    while len(build_order) != num_projects:
        for project, dependencies in dependency_list.items():
            if len(dependencies) == 0 and project not in build_order:
                build_order.append(project)
            else:
                flag = False
                for i in range(len(dependencies)):
                    if dependencies[i] in build_order:
                        flag = True
                        continue
                    else:
                        flag = False
                        break
                if flag: build_order.append(project)
        print(build_order)
        if len(build_order) == length_last:
            return -1
        length_last = len(build_order)
    return build_order


projects = [[0,1],[1,2],[1,3],[0,2]]

build_order = build_order(projects)

print(build_order)