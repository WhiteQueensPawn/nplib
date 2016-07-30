import re

atom_symbol_pattern = re.compile(
    r"C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|"
    r"H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|"
    r"I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|"
    r"U|V|W|Xe|Yb?|Z[nr]")

count_pattern = re.compile(r"\d+")


def atom_count(s):
    n = len(s)
    count = 0
    pos = 0
    while pos < n:
        # Must have an element
        m = atom_symbol_pattern.match(s, pos)
        if not m:
            raise TypeError("Expecting an element symbol at position %d (%r)" %
                            (pos, s))
        pos = m.end()

        # May have an optional repeat count
        m = count_pattern.match(s, pos)
        if m:
            count += int(m.group())
            pos = m.end()
        else:
            count += 1
    return count


def test():
    assert atom_count("He") == 1
    assert atom_count("H2") == 2
    assert atom_count("H2SO4") == 7
    assert atom_count("CH3COOH") == 8
    assert atom_count("NaCl") == 2
    assert atom_count("C60H60") == 120


if __name__ == "__main__":
    test()
