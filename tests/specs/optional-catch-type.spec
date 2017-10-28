try {
    throw new Exception();
} catch ($e) {
    print $e->getMessage();
}

~~~

try {
    throw new Exception();
} catch (\Exception $e) {
    print $e->getMessage();
}
