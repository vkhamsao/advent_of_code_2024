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
    pattern = ~r/(?:do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)/

    {_final_state, products} =
      file_contents
      |> Enum.reduce({true, []}, fn line, {current_state, all_products} ->
        {new_state, line_products} =
          Regex.scan(pattern, line)
          |> Enum.reduce({current_state, []}, fn
            ["do()" | _], {_, muls} ->
              {true, muls}

            ["don't()" | _], {_, muls} ->
              {false, muls}

            [_full, num1, num2], {true, muls} ->
              product = String.to_integer(num1) * String.to_integer(num2)
              {true, [product | muls]}

            [_full, _num1, _num2], {false, muls} ->
              {false, muls}
          end)

        {new_state, line_products ++ all_products}
      end)

    Enum.sum(products)
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
      |> IO.puts()
    end
  end
end

if System.argv() != [] do
  Multiplier.main(System.argv())
end
