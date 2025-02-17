def solve_csp():
    variables = ['m', 'i', 'k', 'e', 'j', 'a', 'c', 'o', 'n']
    domains = {var: list(range(10)) for var in variables}
    domains['m'] = list(range(1, 10))  # 'm' cannot be 0
    domains['j'] = list(range(1, 10))  # 'j' cannot be 0

    def consistent(assignment):
        return len(set(assignment.values())) == len(assignment.values())

    def solve(assignment):
        if len(assignment) == len(variables):
            return assignment
        var = next(var for var in variables if var not in assignment)
        for value in domains[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if consistent(new_assignment):
                result = solve(new_assignment)
                if result:
                    return result
        return None

    solution = solve({})
    return solution

# Print the solution
solution = solve_csp()
if solution:
    print("Solution found:")
    print("mike =", solution['m'], solution['i'], solution['k'], solution['e'])
    print("jack =", solution['j'], solution['a'], solution['c'], solution['k'])
    print("john =", solution['j'], solution['o'], solution['h'], solution['n'])
else:
    print("No solution found.")
