#!/usr/bin/env ruby

# Check if the argument matches the pattern /School/
def match_school(arg)
  if arg =~ /School/
    puts "School"
  else
    puts ""
  end
end

# Get the argument from the command line
arg = ARGV[0]

# Call the matching method
match_school(arg)
