import { NextResponse } from 'next/server';

export async function POST(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const { id } = await params;
    const bikeId = parseInt(id);

    return NextResponse.json({ message: 'Ride started successfully' });
  } catch (error) {
    console.error('Error starting ride:', error);
    return NextResponse.json(
      { error: 'Internal server error', message: 'Failed to start ride' },
      { status: 500 }
    );
  }
}

