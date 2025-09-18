# ==== SLICING ====
      # Slicing allows you to extract a portion ( substring ) from string using index positions.

# Syntax :
            # String [ start : end : step ]
                # Start : index to begin ( inclusive )
                # End   : index to stop ( exclusive )
                # Step  : interval between charaters ( optional )



# Slice From the Start
  # Get the characters from the start to position 5 (not included):
a = "chenna kesava"
print(a[:4])     # chen


# Slice To the End
   # By leaving out the end index, the range will go to the end:
#ex:
a = "chenna kesava"
print(a[3:])      # nna kesva


# Negative Indexing
    # Use negative indexes to start the slice from the end of the string:
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2): 
a = "chenna kesava"
print(a[-6:-2])      # kesa



# Reversing 
a = "chenna kesava"
print(a[::-1])           # avasek annehc


# Step slicing
a = "chenna kesava"
print(a[::2])    # cen eaa   --> every 2nd char
print(a[1::2])   # hnaksv    --> from index 1, every 2nd char
