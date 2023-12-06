import Text.Read (readMaybe)
import Data.Char (isDigit)
import Control.Monad.Cont (cont)

cleanText :: String -> String
cleanText = filter isDigit

-- Function to read the file and extract two arrays
readFileAndExtractArrays :: FilePath -> IO (Int, Int)
readFileAndExtractArrays filePath = do
  content <- readFile filePath
  let separated = lines content
  let numbers = fmap (read . cleanText) separated :: [Int]
  return (numbers !! 0, numbers !! 1)
  

f :: Int -> Int -> Int
f total_time distance = length [speed | speed <- [0..total_time-1], let traveled = speed * (total_time - speed), traveled > distance]

main :: IO ()
main = do
  (time, dist) <- readFileAndExtractArrays "input.txt"
  putStrLn "time:"
  print time
  putStrLn "dist:"
  print dist
  let result = f time dist
  putStrLn $ "result: " ++ show result