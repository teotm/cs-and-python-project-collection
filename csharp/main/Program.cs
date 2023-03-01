using System;

namespace MyProgram
{
	class Program
	{
		static void Main(string[] args)
		{
			string[] a = {
				"Hello, World!",
				"Hello boy, what are you doing in here?",
				"I'm going insane!!! WRAAAAHH",
				"Goodbye world :("
			};

			Random random = new Random();

			int b = random.Next(0, a.Length);
			Console.WriteLine(a[b]);
			Console.ReadLine();
		}
	}
}