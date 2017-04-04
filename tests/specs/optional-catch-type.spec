--DESCRIPTION--

Test optional catch type

--GIVEN--

try {
    throw new Exception();
} catch ($e) {
    print $e->getMessage();
}

--EXPECT--

try {
    throw new Exception();
} catch (\Exception $e) {
    print $e->getMessage();
}
