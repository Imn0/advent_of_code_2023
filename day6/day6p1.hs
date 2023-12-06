import Text.Read (readMaybe)

-- Function to parse a line of text into an array of integers
parseLine :: String -> Maybe [Int]
parseLine line = traverse readMaybe (words line)

-- Function to extract values after ':' in a line
extractValues :: String -> Maybe [Int]
extractValues line = case dropWhile (/= ':') line of
  ':' : rest -> parseLine rest
  _ -> Nothing


-- Function to read the file and extract two arrays
readFileAndExtractArrays :: FilePath -> IO ([Int], [Int])
readFileAndExtractArrays filePath = do
  content <- readFile filePath
  let [textLine, otherTextLine] = lines content
  let timeArr = case extractValues textLine of
        Just arr -> arr
        Nothing -> error "Failed to parse text line"
  let distArr = case extractValues otherTextLine of
        Just arr -> arr
        Nothing -> error "Failed to parse other text line"
  return (timeArr, distArr)

f :: Int -> Int -> Int
f total_time distance = length [speed | speed <- [0..total_time-1], let traveled = speed * (total_time - speed), traveled > distance]

main :: IO ()
main = do
  (timeArr, distArr) <- readFileAndExtractArrays "smol.txt"
  putStrLn "time:"
  print timeArr
  putStrLn "dist:"
  print distArr
  let result = foldl (*) 1 $ zipWith f timeArr distArr
  putStrLn $ "result: " ++ show result