print("🧬 DNA SEQUENCE ANALYZER 🧬")
print("=" * 35)

dna = input("Enter DNA sequence (A/T/G/C): ").upper()

# Check the sequence
valid = True

for base in dna:
    if base not in "ATGC":
        valid = False
        break

if not valid:
    print("❌ Invalid DNA sequence!")

else:
    print("\n🔬 Analyzing...")

    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    gc = ((g + c) / len(dna)) * 100

    print("\n📊 RESULTS")
    print("-" * 25)
    print("A (Adenine):", a)
    print("T (Thymine):", t)
    print("G (Guanine):", g)
    print("C (Cytosine):", c)
    print("GC Percentage:", round(gc, 2), "%")

    print("\n✅ Analysis Complete!")