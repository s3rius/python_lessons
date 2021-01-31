def dec_to_binary(
    thought: int,
) -> str:
    """
    Convert integer to binary string.

    Let's talk as a computers. Your task is to convert
    computer's thoughts (integer value) into the
    computer message in binary format (str).
    The "Binary" means that your message have only 1s and 0s.

    Your function must work as the following:
    >>> message = dec_to_binary(339)
    >>> print(message)
    >>> "101010011"

    :param thought: thought is a number >= 0.
    :return: binary string.
    """
    return ""  # Write your solution here.


def hamming_distance(
    first_dna: str,
    second_dna: str,
) -> int:
    """
    Calculate hamming distance.

    Your body is made up of cells that contain DNA.
    Those cells regularly wear out and need replacing,
    which they achieve by dividing into daughter cells.
    In fact, the average human body experiences about 10 quadrillion
    cell divisions in a lifetime!

    When cells divide, their DNA replicates too.
    Sometimes during this process mistakes happen and single pieces
    of DNA get encoded with the incorrect information.
    If we compare two strands of DNA and count the differences between
    them we can see how many mistakes occurred.
    This is known as the "Hamming Distance".

    The Hamming Distance is useful for lots of things in science,
    not just biology, so it's a nice phrase to be familiar with :)
    We read DNA using the letters C,A,G and T.
    Two strands might look like this:
    first_dna:  "GAGCCTACTAACGGGAT"
    second_dna: "CATCGTAATGACGGCCT"
    difference:  ^ ^ ^  ^ ^    ^^

    They have 7 differences, and therefore the Hamming Distance is 7
    and you must return 7.

    :param first_dna: dna sequence with length > 0.
    :param second_dna: dna sequence with length > 0.
    :return: hamming distance.
    """
    return 0  # Write your solution here.
