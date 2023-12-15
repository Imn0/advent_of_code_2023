with Ada.Text_IO; use Ada.Text_IO;

with Ada.Strings.Unbounded;
use Ada.Strings.unbounded;

procedure day15p2 is

   type BoxMember is record
      Label : Unbounded_String; 
      focal_length : Integer;
   end record;


   type TwoDIntArr is array (Positive range <>, Positive range <>) of Integer;
   type BoxArray is array (Positive range <>, Positive range <>) of BoxMember;
   type IntArr is array (Positive range <>) of Integer;
   input_data : TwoDIntArr(1..4050, 1..20);
   boxes      : BoxArray(1..256, 1..250) := (others => (others => (To_Unbounded_String(""), 0)));
   total_len  : Integer := 1; 
   total_answ : Integer := 0;


   procedure CalculateAnswer is
   current_pos : Integer := 1;   
   begin
      for I in 1..256 loop
         current_pos := 1;   
         for J in 1..250 loop
            if boxes(I, J).Label /= To_Unbounded_String("") then
               total_answ := total_answ + ( (I) *  (current_pos) * (boxes(I, J).focal_length) );
               current_pos := current_pos + 1;
            end if;
         end loop;
      end loop;
   end CalculateAnswer;

   procedure UpdateBox(box: Integer; focal_length : Integer; label : Unbounded_String) is
   
   begin
      if focal_length = 0 then            
         for J in 1..250 loop
            if boxes(box, J).Label = label then
               boxes(box, J).Label := To_Unbounded_String("");
               boxes(box, J).focal_length := 0;
               return;
            end if;
         end loop;   
         return;
      end if;

      for J in 1..250 loop
         if boxes(box, J).Label = label then
            boxes(box, J).focal_length := focal_length;
            return;
         end if;
      end loop;
      
      for J in reverse 1..250 loop
         if boxes(box, J).Label /= To_Unbounded_String("") then
            boxes(box, J+1).Label := label;
            boxes(box, J+1).focal_length := focal_length;
            return;
         end if;
      end loop;

      boxes(box, 1).Label := label;
      boxes(box, 1).focal_length := focal_length;


   end UpdateBox;

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
         elsif value = '-' then
            input_data(total_len, current_str) := Character'Pos('=');
            current_str := current_str + 1;
            input_data(total_len, current_str) := Character'Pos('0');
            current_str := current_str + 1;
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
      focal_length : Integer := 0;
      label : Unbounded_String := To_Unbounded_String("");
   begin
      for J in 1..total_len loop
         I := 1;
         label := To_Unbounded_String("");
         current := 0;
         while input_data(J, I) /= 0 loop
            if input_data(J, I) = Character'Pos('=') then
               UpdateBox(current + 1, input_data(J, I+1) - Character'Pos('0'), label);
            end if;
            Append(label, Character'Val(input_data(J, I)));
            current := current + input_data(J, I);
            current := current * 17;
            current := current mod 256;
            I := I + 1;
         end loop;
      end loop;
   end Hash;

begin
   ReadFile;
   Hash;
   CalculateAnswer;
   Put_Line(Integer'Image(total_answ));
end day15p2;
