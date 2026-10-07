-- Part A: Functional Programming (Haskell)
-- Learning Performance Analysis

-- Each learner has: Student ID, Name, and a list of module scores.
type Student = (String, String, [Double])


students :: [Student]
students =
    [ ("AM001", "Hana",   [75, 60, 70])  -- Normal Case (Avg: 68.33)
    , ("AM002", "Achik",  [85, 90, 90])  -- Normal Case (Avg: 88.33)
    , ("AM003", "Aina",   [60, 75, 70])  -- Normal Case (Avg: 68.33)
    , ("AM004", "Amin",   [60, 65, 70])  -- Normal Case (Avg: 65.00)
    , ("AM005", "Zafran", [90, 95, 90])  -- Tie Case 1  (Avg: 91.67)
    , ("AM006", "Adam",   [85, 90, 80])  -- Normal Case (Avg: 85.00)
    , ("AM007", "Farah",  [80, 80, 80])  -- Boundary Case (Avg: Exactly 80.00)
    , ("AM008", "Sara",   [90, 95, 90])  -- Tie Case 2  (Avg: 91.67)
    ]



averageGrade :: [Double] -> Double
averageGrade grades =
    sum grades / fromIntegral (length grades)

studentAverage :: Student -> (String, String, Double)
studentAverage (studentID, name, grades) =
    (studentID, name, averageGrade grades)



distinctionStudents :: [Student] -> [(String, String, Double)]
distinctionStudents studentList =
    filter (\(_, _, avg) -> avg >= 80)
    (map studentAverage studentList)



topStudent :: [Student] -> (String, String, Double)
topStudent studentList =
    foldl1
        (\student1 student2 ->
            if third student1 > third student2
            then student1
            else student2)
        (map studentAverage studentList)
    where
        third (_, _, x) = x


main :: IO ()
main = do
    putStrLn "=========================================="
    putStrLn "    STUDENT GRADE ANALYSIS (HASKELL)      "
    putStrLn "=========================================="

    putStrLn "\n--- 1. All Student Averages (Normal & Test Data) ---"
    mapM_ print (map studentAverage students)

    putStrLn "\n--- 2. High-Achieving Students (Average >= 80) ---"
    putStrLn "[Boundary Test Note: Farah (Avg 80.0) IS included due to '>= 80']"
    mapM_ print (distinctionStudents students)

    putStrLn "\n--- 3. Top-Performing Student ---"
    putStrLn "[Tie Test Note: Zafran & Sara both scored 91.67."
    putStrLn " Tie Rule applied: The later record in list (Sara) is selected.]"
    print (topStudent students)