# %%
import csv

# %%
def read_csv_sim_file(file_name):
    """The format of the csv file must match the one provided in the example csv file,
    which in turn follows the original xls structure.
    """
    sims = {}
    with open(file_name, newline="") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        header = next(csv_reader, None)  # read the headers
        for row in csv_reader:
            simulation_name = row[0]
            sims[simulation_name] = {k: v for k, v in zip(header, row)}
    return sims


# %%
sim_config = read_csv_sim_file("CoreMapperDemoParameters.csv")

for i, (run_name, run_config) in enumerate(sim_config.items()):
    # Get inputs for model run
    outputBaseName = run_name
    habitatRaster = run_config["habitat_raster_file"]
    resistanceRaster = run_config["resistance_raster_file"]
    outputBaseFolder = run_config["output_directory"]

    movingWindowRadius = run_config["moving_window_radius"]  ## Euclidean distance
    minAvgHabValue = run_config[
        "min_average_habitat_value"
    ]  ## used in the moving window
    binaryThreshold = run_config[
        "min_habitat_value_per_pixel"
    ]  ## used to convert habitat model to binary
    expandCWDValue = run_config["expand_cores_CWD_value"]  ## cost-weighted distance
    removeCWDHalos = bool(run_config["trim_back_expanded_cores"])
    minCoreArea = int(run_config["min_core_area_size"])
    stampCores = bool(
        run_config["exclude_nonhabitat_from_core_size_calcs"]
    )  ## used to convert habitat model to binary
    appendCoreStats = bool(run_config["append_core_stats"])
    deleteIntermediates = bool(run_config["delete_temporary_files"])

    print(
        f"{outputBaseName}, {habitatRaster}, {resistanceRaster}, {outputBaseFolder}, ",
        f"{movingWindowRadius}, {minAvgHabValue}, {binaryThreshold}, {expandCWDValue}, "
        f"{removeCWDHalos}, {minCoreArea}, {stampCores}, {appendCoreStats}, {deleteIntermediates}",
    )

# %%
