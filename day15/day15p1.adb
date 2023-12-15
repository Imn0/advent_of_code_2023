with Ada.Text_IO; use Ada.Text_IO;


procedure day15p1 is
   type Input_Array is array (Positive range <>, Positive range <>) of Integer;
   input_data : Input_Array(1..4050, 1..20);
   total_len  : Integer := 1; 
   total_answ : Integer := 0;

   procedure ReadFile is
      Input_File    : File_Type;
      value         : Character;
      current_str   : Integer := 1;
   begin
      Ada.Text_IO.Open (File => Input_File, Mode => Ada.Text_IO.In_File, Name => "input.txt");

      while not End_OF_File (Input_File) loop
         Ada.Text_IO.Get (File => Input_File, Item => value);
         if value = ',' then
            input_data(total_len, current_str) := 0;
            total_len := total_len + 1;
            current_str := 1;
         else 
            input_data(total_len, current_str) := Character'Pos(value);
            current_str := current_str + 1;
         end if;
      end loop;
      Ada.Text_IO.Close (File => Input_File);
   end ReadFile;

   procedure Hash is   
      I : Integer := 1;
      current : Integer := 0;
   begin
      for J in 1..total_len loop
         I := 1;
         current := 0;
         while input_data(J, I) /= 0 loop
            current := current + input_data(J, I);
            current := current * 17;
            current := current mod 256;
            I := I + 1;
         end loop;
         total_answ := total_answ + current;
      end loop;
   end Hash;

begin
   ReadFile;
   Hash;
   Put(Integer'Image(total_answ));
end day15p1;
