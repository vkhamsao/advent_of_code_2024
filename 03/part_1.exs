#!/usr/bin/env elixir

defmodule Multiplier do
  def process_data(filename) do
    case File.read(filename) do
      {:ok, content} ->
        content
        |> String.split("\n", trim: true)

      {:error, reason} ->
        IO.puts("Error reading file: #{:file.format_error(reason)}")
        {:error, reason}
    end
  end

  @doc """
  Process the file contents with a regex looking
  for expected mul pattern. Returns three dimensional
  list of with matches.
  """
  def regex_processor(file_contents) do
    file_contents
    |> Enum.map(fn line ->
      Regex.scan(~r/mul\((\d{1,3}),(\d{1,3})\)/, line, capture: :all_but_first)
    end)
  end

  def inner_multiply_and_sum(list) do
    list
    |> Enum.map(fn line ->
      line
      |> Enum.map(fn [num1, num2] ->
        String.to_integer(num1) * String.to_integer(num2)
      end)
      |> Enum.sum()
    end)
    |> IO.inspect()
  end

  def main(args) do
    {opts, _, _} =
      OptionParser.parse(args,
        switches: [file: :string],
        aliases: [f: :file]
      )

    filename = Keyword.get(opts, :file)

    if is_nil(filename) do
      IO.puts("Please provide a filename with --file or -f")
    else
      process_data(filename)
      |> regex_processor()
      |> inner_multiply_and_sum()
      |> Enum.sum()
      |> IO.puts()
    end
  end
end

if System.argv() != [] do
  Multiplier.main(System.argv())
end
