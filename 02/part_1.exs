#!/usr/bin/env elixir

defmodule ReportChecker do
  def process_data(filename) do
    case File.read(filename) do
      {:ok, content} ->
        content
        |> String.split("\n", trim: true)
        |> Enum.map(fn line ->
          line
          |> String.split()
          |> Enum.map(&String.to_integer/1)
        end)

      {:error, reason} ->
        IO.puts("Error reading file: #{:file.format_error(reason)}")
        {:error, reason}
    end
  end

  def is_safe?(list) do
    diffs =
      list
      |> Enum.chunk_every(2, 1, :discard)
      |> Enum.map(fn [a, b] -> b - a end)

    all_positive = Enum.all?(diffs, fn x -> x >= 1 and x <= 3 end)
    all_negative = Enum.all?(diffs, fn x -> x >= -3 and x <= -1 end)
    all_positive or all_negative
  end

  def count_safe(list) do
    safe_count =
      list
      |> Enum.count(&is_safe?/1)

    IO.puts("Safe count: #{safe_count}")
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
      |> count_safe()
    end
  end
end

if System.argv() != [] do
  ReportChecker.main(System.argv())
end
