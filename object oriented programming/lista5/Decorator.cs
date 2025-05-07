// dynamically adding functionalities to objects without changing the original code

using System;
using System.IO;

// shifiting data from a stream during reading and writing
public class CaesarStream : Stream
{
    private readonly Stream _baseStream;
    private readonly int _shift; //shift value for the ceasar shipher
    private readonly bool _leaveOpen;    // are we leaving the base stream open when this stream is disposed

    public CaesarStream(Stream baseStream, int shift, bool leaveOpen = false) //constructor
    {
        _baseStream = baseStream ?? throw new ArgumentNullException(nameof(baseStream));
        _shift = shift;
        _leaveOpen = leaveOpen;
    }

    //what the stream can do
    public override bool CanRead => _baseStream.CanRead;
    public override bool CanSeek => false;

    public override bool CanWrite => _baseStream.CanWrite;

    public override long Length => _baseStream.Length;

    // position in the base stream
    public override long Position
    {
        get => _baseStream.Position;
        set => throw new NotSupportedException()
    }

    public override void Flush() => _baseStream.Flush();

    // offset - where to start reading from the buffer.
    public override int Read(byte[] buffer, int offset, int count)
    {
        int readCount = _baseStream.Read(buffer, offset, count);
        for (int i = offset; i < offset + readCount; i++)
        {
            buffer[i] = (byte)(buffer[i] + _shift);
        }
        return readCount;
    }

    //writes data to the basestream
    public override void Write(byte[] buffer, int offset, int count)
    {
        byte[] shifted = new byte[count];
        for (int i = 0; i < count; i++)
        {
            shifted[i] = (byte)(buffer[offset + i] + _shift);
        }
        _baseStream.Write(shifted, 0, count);
    }
    public override long Seek(long offset, SeekOrigin origin) =>
        throw new NotSupportedException();

    public override void SetLength(long value) =>
        _baseStream.SetLength(value);

    protected override void Dispose(bool disposing)
    {
        if (disposing && !_leaveOpen)
            _baseStream.Dispose();

        base.Dispose(disposing);
    }
}
